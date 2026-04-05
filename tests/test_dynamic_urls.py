import pytest


@pytest.mark.asyncio
async def test_update_stocks_dynamic_url(mock_aioresponse, wb_client):
    """Проверка динамического формирования URL и исключения полей из Payload."""

    warehouse_id = 15678
    # Ожидаем PUT запрос на правильный URL
    url = f"https://marketplace-api.wildberries.ru/api/v3/stocks/{warehouse_id}"

    mock_aioresponse.put(
        url, status=200, payload={}
    )  # WB возвращает 200/204 при успехе

    # Выполняем запрос
    result = await wb_client.update_stocks(
        warehouse_id=warehouse_id, stocks=[{"chrtId": 12345, "amount": 10}]
    )

    assert result is True

    # ПРОВЕРКА PAYLOAD'А: убеждаемся, что warehouse_id НЕ попал в JSON тело
    request_call = list(mock_aioresponse.requests.values())[0][0]
    sent_json = request_call.kwargs.get("json")

    assert "warehouse_id" not in sent_json
    assert "stocks" in sent_json
    assert sent_json["stocks"][0]["chrtId"] == 12345
