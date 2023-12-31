import pytest

from project.app import create_app


@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_request_status(client):
    response = client.get("/")
    assert response.status_code == 200


def test_request_error(client):
    response = client.get("/")
    assert b"error" not in response.data.lower()


def test_route_login(client):
    response = client.get("/login")
    assert b"Login" in response.data
