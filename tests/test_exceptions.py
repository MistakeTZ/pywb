import pytest
from pywb.exceptions import TooManyRequestsError, ClientDecodeError


@pytest.mark.asyncio
async def test_429_too_many_requests(mock_aioresponse, wb_client):
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/api/v1/seller-info",
        status=429,
        payload={"title": "too many requests", "detail": "limited"},
    )

    with pytest.raises(TooManyRequestsError) as exc:
        await wb_client.get_seller_info()

    assert exc.value.status_code == 429


@pytest.mark.asyncio
async def test_invalid_json_response(mock_aioresponse, wb_client):
    """Тест: WB вернул сломанный JSON или HTML."""
    mock_aioresponse.get(
        "https://common-api.wildberries.ru/api/v1/seller-info",
        status=200,
        body="<html>502 Bad Gateway</html>",
    )

    with pytest.raises(ClientDecodeError):
        await wb_client.get_seller_info()
