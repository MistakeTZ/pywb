## pywb

Asynchronous Python client for working with the Wildberries Seller API.

The library provides:

- async HTTP client based on `aiohttp`
- typed request/response models via `pydantic`
- centralized API error mapping to Python exceptions
- support for multiple Wildberries API domains

## Features

- Easy entry point through `WBClient`
- Domain routing (`common`, `content`, `statistics`, etc.)
- Built-in methods:
  - ping (`client.ping()`)
  - content ping (`client.ping_content()`)
  - statistics orders report (`client.get_orders(...)`)
  - etc.
- Generic low-level method execution:
  - `await client(SomeWBMethod(...))`
- Context manager support:
  - `async with WBClient(...) as client:`

## Requirements

- Python 3.12+

## Installation

Using `uv`:

```bash
uv add python-wb
```

With `pip`:

```bash
pip install python-wb
```

## Quick Start

```python
import asyncio
from pywb import WBClient


async def main() -> None:
    token = "YOUR_WB_API_TOKEN"

    async with WBClient(token) as client:
        result = await client.ping()
        print(result.ts, result.status)


if __name__ == "__main__":
    asyncio.run(main())
```

## Usage

### 1) Health check

```python
result = await client.ping()
print(result.status)
```

### 2) Content API health check

```python
result = await client.ping_content()
print(result.status)
```

### 3) Get orders from Statistics API

```python
from datetime import datetime

orders = await client.get_orders(
    date_from=datetime(2026, 1, 1, 0, 0, 0),
    flag=0,
)

if orders:
    print(orders[0].srid, orders[0].brand)
```

`date_from` accepts either:

- ISO 8601 string (example: `"2022-03-04T18:08:31"`)
- `datetime` object

## Low-Level Method Call

You can call method objects directly through the client:

```python
from pywb.methods import Ping

response = await client(Ping())
```

This is useful when adding new method classes while keeping one transport layer.

## Error Handling

HTTP errors are mapped to dedicated exceptions:

- `BadRequestError` (400)
- `UnauthorizedError` (401)
- `PaymentRequiredError` (402)
- `AccessDeniedError` (403)
- `NotFoundError` (404)
- `ConflictError` (409)
- `PayloadTooLargeError` (413)
- `UnprocessableEntityError` (422)
- `TooManyRequestsError` (429)
- `InternalServerError` (5xx)

Base type: `WBApiError`

Example:

```python
from pywb.exceptions import BadRequestError

try:
    await client.get_orders(date_from="2022-03-04T18:08:31")
except BadRequestError as e:
    print(e)
    print(e.payload)
```

Network/transport failures in the `aiohttp` session are raised as `WBNetworkError`.

## Sandbox and Domains

The client supports domain-based URL routing through `WBDomain` and `WB_ROUTER`.

To enable sandbox mode (only where available for a domain):

```python
client = WBClient(token="YOUR_TOKEN", is_sandbox=True)
```

If sandbox is unavailable for a domain, a `ValueError` is raised by the session router.

## Development

Run the example script:

```bash
python examples/ping.py
```

## Notes

- Keep your API token secret and do not commit it to git.
- Respect Wildberries API rate limits for each endpoint.
- For the statistics orders endpoint, use pagination strategy based on the last record timestamp when handling large datasets.
