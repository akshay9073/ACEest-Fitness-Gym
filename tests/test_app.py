from Aceestver_3_2_4 import app

client = app.test_client()

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200

def test_dashboard():
    response = client.get("/dashboard")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_members():
    response = client.get("/members")
    assert response.status_code == 200

def test_trainers():
    response = client.get("/trainers")
    assert response.status_code == 200