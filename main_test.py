from main import app, db_connection
from fastapi.testclient import TestClient
client = TestClient(app)
db_connection.autocommit = False

def test_read_spelers():
    response = client.get("/spelers")
    assert response.status_code == 200
    assert response.json() != []

def test_read_teams():
    response = client.get("/teams")
    assert response.status_code == 200
    assert response.json() != []

def test_read_competities():
    response = client.get("/competities")
    assert response.status_code == 200
    assert response.json() != []

def test_create_competities():
    response = client.post("/competities?competitienaam=Serie+B&competitieland=Italië")
    assert response.status_code == 200

def test_create_spelers():
    response = client.post("/spelers?spelernaam=Hans&spelerland=Spanje&spelerleeftijd=22&spelerstatistiek=60&teamid=1")
    assert response.status_code == 200

def test_create_teams():
    response = client.post("/teams?teamnaam=bayern+munchen&competitie_id=1")
    assert response.status_code == 200

def test_delete_speler():
    response = client.delete("/spelers/24")
    assert response.status_code == 200

def test_put_speler():
    response = client.put("/spelers/24?spelerleeftijd=22&spelerstatistiek=60&teamid=1")
    assert response.status_code == 200

