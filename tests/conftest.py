import pytest
from aioresponses import aioresponses
from pywb import WBClient


@pytest.fixture
def mock_aioresponse():
    """Фикстура для перехвата HTTP-запросов aiohttp."""
    with aioresponses() as m:
        yield m


@pytest.fixture
async def wb_client():
    """Фикстура для создания клиента."""
    async with WBClient(token="test_token_123") as client:
        yield client
