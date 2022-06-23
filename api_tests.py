import requests

API_URL = "http://34.245.151.68:8000"

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
	
def test_model_predict():
    response = requests.post(
        url=f"{API_URL}/predict",
		params={'tenure': 29,
            'paperless_billing': 1,
            'internet_service_fiber_optic': 0,
            'no_internet_service': 1,
            'online_security': 0,
            'device_protection': 0,
            'contract_month_to_month': 0,
            'payment_method_electronic_check': 1}
        # url="{}/predict".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data["prediction"] == 0
