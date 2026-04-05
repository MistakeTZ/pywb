import pytest
from pydantic import ValidationError

from pywb.types import DateFilterRequest, SuppliesFiltersRequest


def test_fbw_filters_accept_python_field_names_and_dump_aliases():
    filters = SuppliesFiltersRequest(
        dates=[
            DateFilterRequest(
                from_date="2026-04-04",
                till="2026-04-05",
                type="createDate",
            )
        ],
        status_ids=[1, 2],
    )

    assert filters.dates is not None
    assert filters.dates[0].from_date == "2026-04-04"

    assert filters.model_dump(by_alias=True, exclude_none=True) == {
        "dates": [
            {
                "from": "2026-04-04",
                "till": "2026-04-05",
                "type": "createDate",
            }
        ],
        "statusIDs": [1, 2],
    }


def test_fbw_date_filter_rejects_datetime_strings():
    with pytest.raises(ValidationError):
        DateFilterRequest(
            from_date="2026-04-04T12:00:00",
            till="2026-04-05",
            type="createDate",
        )