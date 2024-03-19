from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_spelers():
    response = client.get("/spelers/")
    assert response.status_code == 200
    assert response.json() == [  {
    "id_speler": 1,
    "naam_speler": "Laurens",
    "leeftijd": 24,
    "afkomst": "Nederland",
    "statistieken": 55,
    "transferwaarde": 20,
    "naam_team": "Ajax"
  },
  {
    "id_speler": 2,
    "naam_speler": "Lean",
    "leeftijd": 20,
    "afkomst": "Nederland",
    "statistieken": 80,
    "transferwaarde": 20,
    "naam_team": "Liverpool"
  },
  {
    "id_speler": 3,
    "naam_speler": "Sam",
    "leeftijd": 20,
    "afkomst": "Nederland",
    "statistieken": 99,
    "transferwaarde": 21,
    "naam_team": "Az"
  }]
