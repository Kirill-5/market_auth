import uuid

from httpx import AsyncClient


async def test_trace_id_echoed_from_request_header(client: AsyncClient) -> None:
    resp = await client.get("/internal/users/999", headers={"X-Trace-Id": "demo-123"})

    assert resp.headers["X-Trace-Id"] == "demo-123"


async def test_trace_id_generated_when_missing(client: AsyncClient) -> None:
    resp = await client.get("/internal/users/999")

    generated = resp.headers["X-Trace-Id"]
    assert uuid.UUID(generated)
