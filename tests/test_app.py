from app import app

def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello! Welcome to my DevOps project." in response.data

def test_health_check():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
