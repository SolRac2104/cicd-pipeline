from app.app import home

def test_home():
    response = home()
    assert response["message"] == "CI/CD working!"
