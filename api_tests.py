import requests

API_URL = "http://127.0.0.1:8000"

def test_model_info():
    response = requests.get(
        url=f"{API_URL}/"
        # url="{}/".format(API_URL)
    )

    assert response.status_code == 200, response.content
	
def test_service_health():
    response = requests.get(
        url=f"{API_URL}/health"
        # url="{}/health".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data["health"] == "ok"
from app.main import api
from fastapi.testclient import TestClient	
def test1_model_predict():	
    client = TestClient(api)

    Input={
           'tenure': 29,
            'paperless_billing': 1,
            'internet_service_fiber_optic': 0,
            'no_internet_service': 1,
            'online_security': 0,
            'device_protection': 0,
            'contract_month_to_month': 0,
            'payment_method_electronic_check': 1}
    response = client.post('/predict', json=input)
    assert response.status_code == 200, response.content
    data = response.json()

    assert data["prediction"] == 0	
Input={
           'tenure': 29,
            'paperless_billing': 1,
            'internet_service_fiber_optic': 0,
            'no_internet_service': 1,
            'online_security': 0,
            'device_protection': 0,
            'contract_month_to_month': 0,
            'payment_method_electronic_check': 1}
def test_model_predict():
    response = requests.post(
        url=f"{API_URL}/predict",
	params="{'input':{}}".format(Input)
        # url="{}/predict".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data["prediction"] == 0
