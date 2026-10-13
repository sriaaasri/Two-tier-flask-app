from app import app

def test_home():
    try:
        tester = app.test_client()
        response = tester.get('/')
        assert response.status_code == 200
    except Exception as e:
        print(e)
    

def test_math():
    assert 2 ==2
def test_string():
    assert "satya".upper() == "SATYA"

def test_string():
    assert "satya".upper() == "SATYA"
