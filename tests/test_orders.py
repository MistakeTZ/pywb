import pytest


@pytest.mark.asyncio
async def test_get_new_orders_fbs(mock_aioresponse, wb_client):
    """Тест парсинга вложенного списка заказов FBS."""
    mock_aioresponse.get(
        "https://marketplace-api.wildberries.ru/api/v3/orders/new",
        payload={
            "orders": [
                {
                    "id": 111,
                    "rid": "rid123",
                    "createdAt": "2024-01-01T10:00:00Z",
                    "warehouseId": 1,
                    "officeId": 2,
                    "nmId": 3,
                    "chrtId": 4,
                    "price": 100,
                    "convertedPrice": 100,
                    "currencyCode": 643,
                    "convertedCurrencyCode": 643,
                    "cargoType": 1,
                    "article": "art",
                    "colorCode": "color",
                    "deliveryType": "fbs",
                    "skus": ["sku1"],
                    "comment": "",
                    "isZeroOrder": False,
                    "crossBorderType": 0,
                }
            ]
        },
        status=200,
    )
    result = await wb_client.get_new_orders()
    assert len(result.orders) == 1
    assert result.orders[0].id == 111
    assert result.orders[0].delivery_type == "fbs"


@pytest.mark.asyncio
async def test_confirm_orders_dbs(mock_aioresponse, wb_client):
    """Тест POST запроса с передачей массива ID заказов DBS."""
    mock_aioresponse.post(
        "https://marketplace-api.wildberries.ru/api/marketplace/v3/dbs/orders/status/confirm",
        payload={
            "requestId": "req-123",
            "results": [{"orderId": 12345, "isError": False}],
        },
        status=200,
    )
    result = await wb_client.confirm_orders_dbs(orders_ids=[12345])
    assert result.request_id == "req-123"
    assert result.results[0].order_id == 12345
    assert result.results[0].is_error is False
