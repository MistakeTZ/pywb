import pytest
from aioresponses import aioresponses

from pywb import WBClient
from pywb.exceptions import TooManyRequestsError, UnauthorizedError


# ==========================================
# ФИКСТУРЫ (Настройка окружения)
# ==========================================
@pytest.fixture
def mock_aioresponse():
    """Фикстура для перехвата и мокирования HTTP-запросов aiohttp."""
    with aioresponses() as m:
        yield m


@pytest.fixture
async def wb_client():
    """Фикстура, создающая клиент перед каждым тестом и закрывающая его после."""
    async with WBClient(token="fake_test_token") as client:
        yield client


# ==========================================
# ТЕСТЫ
# ==========================================
@pytest.mark.asyncio
async def test_ping_success(mock_aioresponse, wb_client):
    """Тест 1: Успешный запрос и парсинг простой Pydantic модели."""

    # 1. Настраиваем мок (что должен вернуть "сервер")
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/ping",
        payload={"TS": "2024-08-16T11:19:05+03:00", "Status": "OK"},
        status=200,
    )

    # 2. Выполняем реальный код библиотеки
    result = await wb_client.ping()

    # 3. Проверяем, что Pydantic правильно смапил поля (TS -> ts, Status -> status)
    assert result.status == "OK"
    assert result.ts == "2024-08-16T11:19:05+03:00"


@pytest.mark.asyncio
async def test_unauthorized_error(mock_aioresponse, wb_client):
    """Тест 2: Проверка правильной генерации ошибки 401 (Unauthorized)."""

    # Имитируем ошибку неверного токена от WB
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/ping",
        payload={
            "title": "unauthorized",
            "detail": "token is malformed",
            "status": 401,
        },
        status=401,
    )

    # Проверяем, что клиент выбрасывает именно наше кастомное исключение
    with pytest.raises(UnauthorizedError) as exc_info:
        await wb_client.ping()

    # Проверяем, что в исключение передались правильные данные из JSON
    assert exc_info.value.status_code == 401
    assert "token is malformed" in exc_info.value.detail


@pytest.mark.asyncio
async def test_rate_limit_error(mock_aioresponse, wb_client):
    """Тест 3: Проверка отлова ошибки 429 (Too Many Requests)."""

    mock_aioresponse.get(
        "https://common-api.wildberries.ru/api/v1/tariffs/commission?locale=ru",
        payload={
            "title": "too many requests",
            "detail": "limited by ID",
            "status": 429,
        },
        status=429,
    )

    with pytest.raises(TooManyRequestsError) as exc_info:
        await wb_client.get_commission(locale="ru")

    assert exc_info.value.status_code == 429


@pytest.mark.asyncio
async def test_get_orders_parsing_list(mock_aioresponse, wb_client):
    """Тест 4: Проверка работы TypeAdapter с ответом в виде списка объектов (list[Model])."""

    # Имитируем ответ со списком заказов из API Статистики
    mock_aioresponse.get(
        "https://statistics-api.wildberries.ru/api/v1/supplier/orders?dateFrom=2022-03-04T18:08:31&flag=0",
        payload=[
            {
                "date": "2022-03-04T18:08:31",
                "lastChangeDate": "2022-03-06T10:11:07",
                "warehouseName": "Подольск",
                "warehouseType": "Склад продавца",
                "countryName": "Россия",
                "oblastOkrugName": "ЦФО",
                "regionName": "Московская",
                "supplierArticle": "12345",
                "nmId": 1234567,
                "barcode": "123453559000",
                "category": "Бытовая техника",
                "subject": "Мультистайлеры",
                "brand": "Тест Бренд",
                "techSize": "0",
                "incomeID": 56735459,
                "isSupply": False,
                "isRealization": True,
                "totalPrice": 1887,
                "discountPercent": 18,
                "spp": 26,
                "finishedPrice": 1145,
                "priceWithDisc": 1547,
                "isCancel": True,
                "cancelDate": "2022-03-09T00:00:00",
                "sticker": "926912515",
                "gNumber": "34343462218572569531",
                "srid": "11.rf9ef",
            }
        ],
        status=200,
    )

    # Вызываем метод
    orders = await wb_client.get_orders(date_from="2022-03-04T18:08:31")

    # Проверяем, что TypeAdapter успешно сгенерировал список объектов
    assert isinstance(orders, list)
    assert len(orders) == 1

    order = orders[0]
    # Проверяем маппинг camelCase -> snake_case
    assert order.nm_id == 1234567
    assert order.brand == "Тест Бренд"
    assert order.warehouse_name == "Подольск"
