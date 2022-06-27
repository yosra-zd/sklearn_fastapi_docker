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

#import main
from main import api
from fastapi.testclient import TestClient	
def test_model_predict():	

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
    response = client.post('/predict', json=Input)
    assert response.status_code == 200, response.content
    data = response.json()

    assert data["prediction"] == 0
 def test_batch_predict():	
     client = TestClient(api)

     Input_File="data/batch_churn.csv" 
     response = client.post('/batch_predict', json=Input_file)
     assert response.status_code == 200, response.content
     data = response.json()

     assert data["Predictions"] == "{\"0\":\"No\",\"1\":\"Yes\",\"2\":\"No\",\"3\":\"No\",\"4\":\"No\"}"

