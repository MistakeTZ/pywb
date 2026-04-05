import pytest


@pytest.mark.asyncio
async def test_get_seller_balance(mock_aioresponse, wb_client):
    """Тест баланса продавца (Финансы)."""
    mock_aioresponse.get(
        "https://finance-api.wildberries.ru/api/v1/account/balance",
        payload={"currency": "RUB", "current": 10500.50, "for_withdraw": 5000.00},
        status=200,
    )
    result = await wb_client.get_seller_balance()
    assert result.current == 10500.50
    assert result.for_withdraw == 5000.00


@pytest.mark.asyncio
async def test_deposit_campaign_budget(mock_aioresponse, wb_client):
    """Тест пополнения рекламного бюджета (query параметры)."""
    advert_id = 12345
    # Идентификатор кампании передается в Query URL
    url = f"https://advert-api.wildberries.ru/adv/v1/budget/deposit?id={advert_id}"

    mock_aioresponse.post(url, payload={"total": 2500}, status=200)
    # Пополняем на 1000 руб со счета (0)
    result = await wb_client.deposit_campaign_budget(
        advert_id=advert_id, amount=1000, source_type=0
    )
    assert result.total == 2500

    # Проверяем, что в JSON ушли правильные параметры
    request_call = list(mock_aioresponse.requests.values())[0][0]
    sent_json = request_call.kwargs.get("json")
    assert sent_json["sum"] == 1000
    assert sent_json["type"] == 0
