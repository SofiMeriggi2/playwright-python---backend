import pytest
import logging
from playwright.sync_api import APIRequestContext, Playwright
from typing import Generator

logger = logging.getLogger(__name__)
BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    context = playwright.request.new_context(base_url=BASE_URL)
    logger.info(f"API context created — base URL: {BASE_URL}")
    yield context
    context.dispose()
    logger.info("API context disposed")


@pytest.fixture(scope="session")
def auth_token(api_request_context: APIRequestContext) -> str:
    response = api_request_context.post(
        "/auth",
        data={"username": "admin", "password": "password123"}
    )
    assert response.ok, f"Auth failed: {response.status} {response.text()}"
    data = response.json()
    assert "token" in data, f"Token missing in response: {data}"
    token = data["token"]
    logger.info(f"Auth token obtained: {token[:6]}...")
    return token


@pytest.fixture(scope="function")
def created_booking_id(api_request_context: APIRequestContext, auth_token: str) -> Generator[int, None, None]:
    from data.payloads import Payloads

    response = api_request_context.post(
        "/booking",
        headers={"Content-Type": "application/json"},
        data=Payloads.new_booking()
    )
    assert response.ok, f"Booking creation failed: {response.status} {response.text()}"
    data = response.json()
    assert "bookingid" in data, f"bookingid missing in response: {data}"
    booking_id = data["bookingid"]
    logger.info(f"Booking created — ID: {booking_id}, name: {data['booking']['firstname']} {data['booking']['lastname']}")

    yield booking_id

    try:
        api_request_context.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={auth_token}"}
        )
        logger.info(f"Booking deleted — ID: {booking_id}")
    except Exception as e:
        logger.warning(f"Cleanup failed for booking {booking_id}: {e}")