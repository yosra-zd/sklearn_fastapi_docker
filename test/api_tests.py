import requests,json

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
     #Input="{\"customerID\":{\"0\":\"8773-HHXXX\",\"1\":\"5945-TMRGD\",\"2\":\"7942-YXOOG\",\"3\":\"4598-ABCDE\",\"4\":\"3192-NQECA\"},\"gender\":{\"0\":\"Female\",\"1\":\"Female\",\"2\":\"Male\",\"3\":\"Female\",\"4\":\"Male\"},\"SeniorCitizen\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No\",\"3\":\"Yes\",\"4\":\"No\"},\"Partner\":{\"0\":\"No\",\"1\":\"No\",\"2\":\"No\",\"3\":\"Yes\",\"4\":\"Yes\"},\"Dependents\":{\"0\":\"Yes\",\"1\":\"Yes\",\"2\":\"No\",\"3\":\"Yes\",\"4\":\"No\"},\"tenure\":{\"0\":6,\"1\":1,\"2\":5,\"3\":25,\"4\":68},\"PhoneService\":{\"0\":\"Yes\",\"1\":\"Yes\",\"2\":\"Yes\",\"3\":\"Yes\",\"4\":\"Yes\"},\"MultipleLines\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No\",\"3\":\"No\",\"4\":\"Yes\"},\"InternetService\":{\"0\":\"DSL\",\"1\":\"Fiber optic\",\"2\":\"No\",\"3\":\"Fiber optic\",\"4\":\"Fiber optic\"},\"OnlineSecurity\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No internet service\",\"3\":\"No\",\"4\":\"No\"},\"OnlineBackup\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No internet service\",\"3\":\"Yes\",\"4\":\"Yes\"},\"DeviceProtection\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No internet service\",\"3\":\"Yes\",\"4\":\"Yes\"},\"TechSupport\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No internet service\",\"3\":\"No\",\"4\":\"Yes\"},\"StreamingTV\":{\"0\":\"Yes\",\"1\":\"Yes\",\"2\":\"No internet service\",\"3\":\"Yes\",\"4\":\"Yes\"},\"StreamingMovies\":{\"0\":\"Yes\",\"1\":\"No\",\"2\":\"No internet service\",\"3\":\"No\",\"4\":\"Yes\"},\"Contract\":{\"0\":\"Month-to-month\",\"1\":\"Month-to-month\",\"2\":\"Month-to-month\",\"3\":\"One year\",\"4\":\"Two year\"},\"PaperlessBilling\":{\"0\":\"Yes\",\"1\":\"Yes\",\"2\":\"No\",\"3\":\"Yes\",\"4\":\"Yes\"},\"PaymentMethod\":{\"0\":\"Electronic check\",\"1\":\"Electronic check\",\"2\":\"Mailed check\",\"3\":\"Electronic check\",\"4\":\"Bank transfer (automatic)\"},\"MonthlyCharges\":{\"0\":20,\"1\":80,\"2\":20,\"3\":100,\"4\":117},\"TotalCharges\":{\"0\":35,\"1\":90,\"2\":115,\"3\":2500,\"4\":600}}"
     fpath='data/batch_churn.csv'
     with open(fpath, "rb") as f:
          response = client.post("/batch_predict", files={"file": ("filename", f, "application/vnd.ms-excel")}) 
          assert response.status_code == 200, response.content
          assert response.content == b"customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Predictions\n8773-HHXXX,0,1,0,1,6,1,Yes,DSL,Yes,Yes,Yes,Yes,Yes,Yes,Month-to-month,1,Electronic check,20,35.0,No\n5945-TMRGD,0,0,0,1,1,1,No,Fiber optic,No,No,No,No,Yes,No,Month-to-month,1,Electronic check,80,90.0,Yes\n7942-YXOOG,1,0,0,0,5,1,No,No,No internet service,No internet service,No internet service,No internet service,No internet service,No internet service,Month-to-month,0,Mailed check,20,115.0,No\n4598-ABCDE,0,1,1,1,25,1,No,Fiber optic,No,Yes,Yes,No,Yes,No,One year,1,Electronic check,100,2500.0,Yes\n3192-NQECA,1,0,1,0,68,1,Yes,Fiber optic,No,Yes,Yes,Yes,Yes,Yes,Two year,1,Bank transfer (automatic),117,600.0,No\n"

          #data = response.json()
           #assert data['Predictions']['0'] == "No"
          #assert data['Predictions'] == {'0':"No",'1':"Yes",'2':"No",'3':"Yes",'4':"No"}

