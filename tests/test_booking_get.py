# tests/test_booking_get.py
import pytest
from clients.booking_client import BookingClient


@pytest.mark.smoke
def test_get_all_bookings(api_request_context):
    """GET /booking devuelve lista de reservas."""
    client = BookingClient(api_request_context)
    response = client.get_all_bookings()

    assert response.ok
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.smoke
def test_get_booking_por_id(api_request_context, created_booking_id):
    """GET /booking/{id} devuelve los datos de la reserva."""
    client = BookingClient(api_request_context)
    response = client.get_booking(created_booking_id)

    assert response.ok
    data = response.json()
    assert data["firstname"] == "Sofi"
    assert data["lastname"] == "QA"
    assert data["totalprice"] == 150


@pytest.mark.negative
def test_get_booking_id_inexistente(api_request_context):
    """GET /booking/{id} con ID inexistente devuelve 404."""
    client = BookingClient(api_request_context)
    response = client.get_booking(999999)

    assert response.status == 404