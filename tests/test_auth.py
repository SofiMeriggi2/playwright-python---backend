import pytest


@pytest.mark.smoke
def test_auth_devuelve_token(api_request_context):
    """Verificar que el endpoint de auth devuelve un token válido."""
    response = api_request_context.post(
        "/auth",
        data={"username": "admin", "password": "password123"}
    )

    assert response.ok
    data = response.json()
    assert "token" in data
    assert len(data["token"]) > 0

#preguntar por este
@pytest.mark.negative
def test_auth_credenciales_invalidas(api_request_context):
    """Credenciales incorrectas devuelven mensaje de error."""
    response = api_request_context.post(
        "/auth",
        data={"username": "wrong", "password": "wrong"}
    )

    assert response.ok
    data = response.json()
    assert data.get("reason") == "Bad credentials"