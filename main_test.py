from fastapi.testclient import TestClient
from main import app
from database import db_connection
from spelers import waarde_berekenen

client = TestClient(app)

def test_01_clean_test_database():
    cursor = db_connection.cursor()
    cursor.execute("drop table if exists spelers; ")
    cursor.execute("drop table if exists teams;")
    cursor.execute("drop table if exists competities;")
    cursor.close()
    db_connection.commit()
def test_02_create_tables_test_database():
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE competities(competitie_id SERIAL PRIMARY KEY, naam VARCHAR(255), land VARCHAR(255));")
    cursor.execute("CREATE TABLE teams(team_id SERIAL PRIMARY KEY, naam VARCHAR(255), competitie_id INT, FOREIGN KEY(competitie_id) REFERENCES competities(competitie_id));")
    cursor.execute("CREATE TABLE spelers(speler_id SERIAL PRIMARY KEY, naam VARCHAR(255), land VARCHAR(255), leeftijd SMALLINT, statistiek SMALLINT, team_id INT, FOREIGN KEY(team_id) REFERENCES teams(team_id));")
    cursor.close()
    db_connection.commit()

def test_03_insert_table_competitie():
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO competities(naam, land) VALUES ('Eredivisie', 'Nederland'),('Premier League', 'Engeland'),('La Liga', 'Spanje');")
    cursor.close()
    db_connection.commit()
def test_04_insert_table_team():
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO teams(naam, competitie_id) VALUES ('Ajax', 1), ('Liverpool', 2), ('AZ', 1);")
    cursor.close()
    db_connection.commit()

def test_05_insert_table_speler():
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO spelers(naam, land, leeftijd, statistiek, team_id) VALUES ('Laurens', 'Nederland', 24, 55, 1), ('Lean', 'Nederland',22, 80, 2), ('Sam', 'Nederland', 20, 99, 3);")
    cursor.close()
    db_connection.commit()

def test_06_read_spelers():
    response = client.get("/spelers")
    assert response.status_code == 200
    print(response.json)
    assert response.json() != []

def test_07_read_teams():
    response = client.get("/teams")
    assert response.status_code == 200
    assert response.json() != []

def test_08_read_competities():
    response = client.get("/competities")
    assert response.status_code == 200
    assert response.json() != []

def test_09_create_competities():
    response = client.post("/competities?competitie_naam=Serie+B&competitie_land=Italië")
    assert response.status_code == 200

def test_10_create_spelers():
    response = client.post(
        "/spelers?spelernaam=Hans&spelerland=Spanje&spelerleeftijd=22&spelerstatistiek=60&teamid=1")
    assert response.status_code == 200

def test_11_create_teams():
    response = client.post("/teams?teamnaam=bayern+munchen&competitie_id=1")
    assert response.status_code == 200

def test_12_put_speler():
    response = client.put("/spelers/4?spelerleeftijd=22&spelerstatistiek=60&teamid=1")
    assert response.status_code == 200

def test_13_delete_speler():
    response = client.delete("/spelers/4")
    assert response.status_code == 200

def test_14_put_speler():
    response = client.put("/spelers/1?spelerleeftijd=15&spelerstatistiek=60&teamid=1")
    assert response.status_code == 400

def test_15_put_speler():
    response = client.put("/spelers/1?spelerleeftijd=60&spelerstatistiek=60&teamid=1")
    assert response.status_code == 400
    
def test_16_create_teams():
    response = client.post("/teams?teamnaam=bayern+munchen&competitie_id=5")
    assert response.status_code == 404

def test_17_put_speler():
    response = client.put("/spelers/4?spelerleeftijd=22&spelerstatistiek=60&teamid=7")
    assert response.status_code == 404

def test_18_create_spelers():
    response = client.post(
        "/spelers?spelernaam=Hans&spelerland=Spanje&spelerleeftijd=22&spelerstatistiek=60&teamid=7")
    assert response.status_code == 404

def test_19_create_spelers():
    response = client.post(
        "/spelers?spelernaam=Hans&spelerland=Spanje&spelerleeftijd=15&spelerstatistiek=60&teamid=1")
    assert response.status_code == 404
    
def test_20_create_spelers():
    response = client.post(
        "/spelers?spelernaam=Hans&spelerland=Spanje&spelerleeftijd=60&spelerstatistiek=60&teamid=7")
    assert response.status_code == 404

def test_waarde_berekenen_jonge_speler():
    speler = ("John Doe", "Nederland", 18, 80, 1)  # Voorbeeld van een jonge speler
    assert waarde_berekenen(speler) == 2640000  # Verwachte totale transferwaarde voor een jonge speler

def test_waarde_berekenen_oude_speler():
    speler = ("John Doe", "Nederland", 30, 80, 1)  # Voorbeeld van een oudere speler
    assert waarde_berekenen(speler) == 27200000  # Verwachte totale transferwaarde voor een oudere speler

def test_waarde_berekenen_gemiddelde_speler():
    speler = ("John Doe", "Nederland", 22, 80, 1)  # Voorbeeld van een gemiddelde speler
    assert waarde_berekenen(speler) == 40000000  # Verwachte totale transferwaarde voor een gemiddelde speler

