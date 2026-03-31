# tests/test_booking_put_patch_delete.py
import pytest
from clients.booking_client import BookingClient
from data.payloads import Payloads


def test_actualizar_reserva_completa(api_request_context, created_booking_id, auth_token):
    """PUT /booking/{id} actualiza todos los campos."""
    client = BookingClient(api_request_context)
    response = client.update_booking(
        created_booking_id,
        Payloads.updated_booking(),
        auth_token
    )

    assert response.ok
    data = response.json()
    assert data["lastname"] == "Updated"
    assert data["totalprice"] == 200


def test_actualizar_reserva_parcial(api_request_context, created_booking_id, auth_token):
    """PATCH /booking/{id} actualiza solo los campos enviados."""
    client = BookingClient(api_request_context)
    response = client.partial_update_booking(
        created_booking_id,
        Payloads.partial_update(),
        auth_token
    )

    assert response.ok
    data = response.json()
    assert data["firstname"] == "SofiPatch"
    assert data["totalprice"] == 999
    assert data["lastname"] == "QA"  # campo no modificado sigue igual


@pytest.mark.smoke
def test_eliminar_reserva(api_request_context, auth_token):
    """DELETE /booking/{id} elimina la reserva correctamente."""
    client = BookingClient(api_request_context)

    # Crear reserva específica para este test
    create_response = client.create_booking(Payloads.new_booking())
    booking_id = create_response.json()["bookingid"]

    # Eliminar
    delete_response = client.delete_booking(booking_id, auth_token)
    assert delete_response.status == 201

    # Verificar que ya no existe
    get_response = client.get_booking(booking_id)
    assert get_response.status == 404