from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_saude():
    resposta = cliente.get("/saudável")
    assert resposta.status_code == 200