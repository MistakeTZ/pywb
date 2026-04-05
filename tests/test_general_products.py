import pytest


@pytest.mark.asyncio
async def test_get_seller_info(mock_aioresponse, wb_client):
    """Тест простого GET запроса."""
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/api/v1/seller-info",
        payload={"name": "ИП Тестов", "sid": "123", "tradeMark": "TestBrand"},
        status=200,
    )
    result = await wb_client.get_seller_info()
    assert result.name == "ИП Тестов"
    assert result.trade_mark == "TestBrand"


@pytest.mark.asyncio
async def test_update_stocks(mock_aioresponse, wb_client):
    """Тест PUT запроса с динамическим URL (исключение warehouse_id из body)."""
    warehouse_id = 15678
    url = f"https://marketplace-api.wildberries.ru/api/v3/stocks/{warehouse_id}"

    mock_aioresponse.put(url, status=200, payload={})

    result = await wb_client.update_stocks(
        warehouse_id=warehouse_id, stocks=[{"chrtId": 12345, "amount": 10}]
    )
    assert result is True

    # Проверяем, что в JSON отправлен camelCase (chrtId)
    request_call = list(mock_aioresponse.requests.values())[0][0]
    sent_json = request_call.kwargs.get("json")
    assert "warehouse_id" not in sent_json
    assert sent_json["stocks"][0]["chrtId"] == 12345
