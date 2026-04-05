import pytest


@pytest.mark.asyncio
async def test_get_seller_info(mock_aioresponse, wb_client):
    """Проверка метода получения информации о продавце."""
    
    # Имитируем ответ сервера
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/api/v1/seller-info",
        payload={
            "name": "ИП Тестов",
            "sid": "1234567890",
            "tradeMark": "TestBrand"
        },
        status=200
    )

    result = await wb_client.get_seller_info()

    # Проверяем, что Pydantic сработал правильно (tradeMark -> trade_mark)
    assert result.name == "ИП Тестов"
    assert result.trade_mark == "TestBrand"

@pytest.mark.asyncio
async def test_get_orders_list(mock_aioresponse, wb_client):
    """Проверка метода возврата списка (TypeAdapter)."""
    
    mock_aioresponse.get(
        "https://statistics-api.wildberries.ru/api/v1/supplier/orders?dateFrom=2024-01-01T00:00:00&flag=0",
        payload=[
            {
                "date": "2024-01-01T18:00:00",
                "lastChangeDate": "2024-01-02T10:00:00",
                "supplierArticle": "ART-1",
                "techSize": "42",
                "barcode": "2000000000000",
                # ... остальные обязательные поля для мока ...
                "warehouseName": "Коледино",
                "warehouseType": "Склад WB",
                "countryName": "Россия",
                "oblastOkrugName": "ЦФО",
                "regionName": "Московская",
                "nmId": 123456,
                "category": "Одежда",
                "subject": "Платья",
                "brand": "Test",
                "incomeID": 111,
                "isSupply": True,
                "isRealization": False,
                "totalPrice": 1000,
                "discountPercent": 10,
                "spp": 5,
                "finishedPrice": 850,
                "priceWithDisc": 900,
                "isCancel": False,
                "cancelDate": "0001-01-01T00:00:00",
                "sticker": "123",
                "gNumber": "123",
                "srid": "123"
            }
        ],
        status=200
    )

    orders = await wb_client.get_orders(date_from="2024-01-01T00:00:00")
    
    assert isinstance(orders, list)
    assert len(orders) == 1
    assert orders[0].supplier_article == "ART-1"