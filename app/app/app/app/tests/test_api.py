from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_multiply():
    response = client.get("/multiply?a11=1&a12=2&a21=3&a22=4&b11=5&b12=6&b21=7&b22=8")
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == [[19, 22], [43, 50]]
