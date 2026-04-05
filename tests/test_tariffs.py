import pytest


@pytest.mark.asyncio
async def test_get_box_tariffs_unwrapping(mock_aioresponse, wb_client):
    """Тест автоматической распаковки ответа (result.response.data)."""
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/api/v1/tariffs/box?date=2024-01-01",
        payload={
            "response": {
                "data": {
                    "dtNextBox": "2024-01-02",
                    "dtTillMax": "2024-01-10",
                    "warehouseList": [
                        {
                            "warehouseName": "Коледино",
                            "geoName": "МСК",
                            "boxDeliveryBase": "10",
                            "boxDeliveryLiter": "1",
                            "boxDeliveryCoefExpr": "1",
                            "boxDeliveryMarketplaceBase": "10",
                            "boxDeliveryMarketplaceLiter": "1",
                            "boxDeliveryMarketplaceCoefExpr": "1",
                            "boxStorageBase": "1",
                            "boxStorageLiter": "0.1",
                            "boxStorageCoefExpr": "1",
                        }
                    ],
                }
            }
        },
        status=200,
    )

    # Клиент должен вернуть сразу WarehousesBoxRates
    result = await wb_client.get_box_tariffs(date="2024-01-01")
    assert result.dt_next_box == "2024-01-02"
    assert len(result.warehouse_list) == 1
    assert result.warehouse_list[0].warehouse_name == "Коледино"
