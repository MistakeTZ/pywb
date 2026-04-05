import pytest


@pytest.mark.asyncio
async def test_download_csv_report_file(mock_aioresponse, wb_client):
    """Проверка скачивания ZIP архива (сырые байты)."""

    download_id = "test-uuid-1234"
    url = f"https://seller-analytics-api.wildberries.ru/api/v2/nm-report/downloads/file/{download_id}"

    fake_zip_bytes = b"PK\x03\x04\x14\x00\x00\x00\x08\x00"  # Заголовок ZIP файла

    # Мокаем ответ с сырыми байтами
    mock_aioresponse.get(url, status=200, body=fake_zip_bytes)

    result = await wb_client.download_csv_report_file(download_id=download_id)

    assert isinstance(result, bytes)
    assert result == fake_zip_bytes


@pytest.mark.asyncio
async def test_get_sales_funnel_products_dynamic_schema(mock_aioresponse, wb_client):
    """Проверка метода аналитики с динамической Pydantic схемой (Any)."""

    url = "https://seller-analytics-api.wildberries.ru/api/analytics/v3/sales-funnel/products"

    # Имитируем успешный ответ аналитики
    mock_aioresponse.post(
        url,
        status=200,
        payload={
            "data": {
                "page": {"cards": [{"nmID": 123, "conversions": {"addToCart": 5}}]}
            }
        },
    )

    payload = {
        "selectedPeriod": {"start": "2024-01-01", "end": "2024-01-07"},
        "limit": 50,
        "offset": 0,
    }

    result = await wb_client.get_sales_funnel_products(payload=payload)

    # Проверяем, что вернулся словарь из поля data
    assert isinstance(result, dict)
    assert "page" in result
    assert result["page"]["cards"][0]["conversions"]["addToCart"] == 5
