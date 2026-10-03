"""The generated SDK against a running Pav API: no mocks.

    PAV_API_KEY=... PAV_BASE_URL=http://localhost:8019 uv run --group dev pytest tests

``PAV_BASE_URL`` defaults to production. Every resource's list and get, cursor
paging, the typed errors and the async client.
"""

from __future__ import annotations

import asyncio
import os

import pytest

from pav_bio import AsyncPav, BadRequestError, NotFoundError, Pav, UnauthorizedError

BASE_URL = os.environ.get("PAV_BASE_URL", "https://api.pav.bio")

pytestmark = pytest.mark.skipif(not os.environ.get("PAV_API_KEY"), reason="needs PAV_API_KEY")

#: Resource -> the list row's id field; ``get`` takes that id.
RESOURCES = {
    "programs": "program_id",
    "drugs": "drug_id",
    "companies": "company_id",
    "trials": "nct_id",
    "deals": "deal_id",
    "patents": "family_id",
    "orange_book_products": "record_key",
    "orange_book_patents": "record_key",
    "orange_book_exclusivities": "record_key",
    "purple_book_products": "record_key",
    "orphan_designations": "record_key",
    "warning_letters": "record_key",
    "recalls": "record_key",
    "drug_applications": "application_key",
    "complete_response_letters": "record_key",
    "accelerated_approvals": "record_key",
    "advisory_committee_meetings": "record_key",
}


@pytest.fixture(scope="module")
def client() -> Pav:
    return Pav(base_url=BASE_URL, api_key=os.environ["PAV_API_KEY"])


@pytest.mark.parametrize("resource", sorted(RESOURCES))
def test_every_resource_lists_and_gets(client: Pav, resource: str) -> None:
    id_field = RESOURCES[resource]
    api = getattr(client, resource)
    page = api.list(limit=1)
    row = next(iter(page))
    row_id = getattr(row, id_field)
    detail = api.get(row_id)
    if resource == "drug_applications":
        assert detail.application.application_key == row_id
    else:
        assert getattr(detail, id_field) == row_id


def test_list_pages_follow_the_cursor_without_repeats(client: Pav) -> None:
    pager = client.programs.list(company=["PFE"], view="slim", limit=20)
    seen = []
    for program in pager:
        seen.append(program.program_id)
        if len(seen) == 60:
            break
    assert len(seen) == 60
    assert len(set(seen)) == 60
    first = next(iter(client.programs.list(company=["PFE"], view="slim", limit=20).iter_pages()))
    assert first.response.total >= 60


def test_filters_and_record_keys_with_slashes(client: Pav) -> None:
    recall = next(iter(client.recalls.list(limit=1)))
    assert "/" in recall.record_key
    assert client.recalls.get(recall.record_key).record_key == recall.record_key
    phase3 = client.programs.list(company=["MRNA"], phase=["phase_3"], limit=5)
    assert {p.phase for p in phase3} == {"phase_3"}


def test_errors_are_typed(client: Pav) -> None:
    with pytest.raises(NotFoundError):
        client.programs.get(999_999_999)
    with pytest.raises(NotFoundError):
        client.warning_letters.get("recall:/not/a/warning-letter")
    with pytest.raises(BadRequestError) as bad:
        client.programs.list(phase=["phase_9"])
    assert "phase_9" in str(bad.value.body)
    with pytest.raises(UnauthorizedError):
        Pav(base_url=BASE_URL, api_key="not-a-key").companies.list(limit=1)


def test_async_client() -> None:
    async def run() -> int:
        client = AsyncPav(base_url=BASE_URL, api_key=os.environ["PAV_API_KEY"])
        page = await client.companies.list(ticker=["PFE"], limit=1)
        return len(page.items)

    assert asyncio.run(run()) == 1
