import pytest
from clients.booking_client import BookingClient
from data.payloads import Payloads


@pytest.mark.smoke
def test_crear_reserva(api_request_context, auth_token):
    """POST /booking crea una nueva reserva correctamente."""
    client = BookingClient(api_request_context)
    response = client.create_booking(Payloads.new_booking())

    assert response.ok
    data = response.json()
    assert "bookingid" in data
    assert data["booking"]["firstname"] == "Sofi"
    assert data["booking"]["totalprice"] == 150

    # Teardown manual — este test crea la reserva sin usar la fixture
    client.delete_booking(data["bookingid"], auth_token)


@pytest.mark.negative
def test_crear_reserva_sin_campos_requeridos(api_request_context):
    """POST /booking sin campos requeridos devuelve error."""
    client = BookingClient(api_request_context)
    response = client.create_booking({"firstname": "Sofi"})

    assert response.status == 500