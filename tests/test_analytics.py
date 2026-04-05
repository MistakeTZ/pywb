import pytest


@pytest.mark.asyncio
async def test_sales_funnel_dynamic_schema(mock_aioresponse, wb_client):
    """Тест аналитики с динамическим Pydantic (Any)."""
    mock_aioresponse.post(
        "https://seller-analytics-api.wildberries.ru/api/analytics/v3/sales-funnel/products",
        payload={
            "data": {
                "page": {"cards": [{"nmID": 123, "conversions": {"addToCart": 5}}]}
            }
        },
        status=200,
    )

    payload = {
        "selectedPeriod": {"start": "2024-01-01", "end": "2024-01-07"},
        "limit": 50,
        "offset": 0,
    }
    result = await wb_client.get_sales_funnel_products(payload=payload)

    # Метод возвращает сырой dict из result.data
    assert isinstance(result, dict)
    assert result["page"]["cards"][0]["nmID"] == 123


@pytest.mark.asyncio
async def test_download_csv_report_file(mock_aioresponse, wb_client):
    """Тест скачивания бинарного файла (ZIP-архив)."""
    download_id = "test-uuid"
    url = f"https://seller-analytics-api.wildberries.ru/api/v2/nm-report/downloads/file/{download_id}"

    fake_zip_bytes = b"PK\x03\x04\x14\x00\x00\x00\x08\x00"
    mock_aioresponse.get(url, status=200, body=fake_zip_bytes)

    result = await wb_client.download_csv_report_file(download_id=download_id)
    assert isinstance(result, bytes)
    assert result == fake_zip_bytes
