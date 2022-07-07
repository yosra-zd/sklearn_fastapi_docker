Churn rate is an important indicator for subscription-based companies. Identifying customers who aren’t happy can help managers identify product or pricing plan weak 
points, operation issues, as well as customer preferences and expectations. When you know all that, it’s easier to introduce proactive ways of reducing churn.
The application to be deployed will function via operational use cases:

    Online prediction: This use case generates predictions on a one-by-one basis for each data point (a customer).
    Batch prediction: This use is for generating predictions for a set of observations instantaneously.


In this API we will do an example implementation of a machine learning churn rate prediction system.
It’s essential to deploy your model so that predictions can be made from a trained ML model available to others, whether users, management, or other systems. 
we will use for this purpose Python's Scikit-Learn + FastAPI + Docker.
#Documentation
FastAPI generates automatic documentation, which will also allow us to test the API. To do this, go to http://0.0.0.0:8000/docs.

There is interactive documentation with Swagger UI, respecting OpenAPI specifications. With OpenAPI, we have interactive documentation, but we can also generate API 
code from specifications in YAML or JSON format. The OpenAPI format is becoming a standard for creating APIs. It is programming language agnostic, allowing both humans
and machines to understand how the API works without accessing source code or documentation.

We can test a prediction very simply. we can also test a command line prediction with CURL.
# Dataset
##Churn  Dataset

The dataset can be found in `data/churn.csv`


### Attribute Information:

                'tenure': 2,
                'no_internet_service': False,
                'internet_service_fiber_optic': False,
                'online_security': False,
                'device_protection': False,
                'contract_month_to_month': True,
                'payment_method_electronic_check': True,
                'paperless_billing': True
# Virtual Environment

Firt we need to create a virtual environment for the project, to keep track of every dependency, it is also useful to use and explicit version of Python

Install the package for creating a virtual environment:
`$ pip install virtualenv`

Create a new virtual environment
`$ virtualenv venv`

Activate virtual environment
`$ source venv/bin/activate`

# Python packages

Now with the virtual environment we can install the dependencies written in requirements.txt

`$ pip install -r requirements.txt`

# Train

After we have installed all the dependencies we can now run the script in code/train.py, this script takes the input data and outputs a trained model and a pipeline for our web service.

`$ python train/train.py`

The model will be saved in the `model` directory

#API endpoints
the script main.py fbased on script functions.py (under ms directory) is used for below endpoints definition:
1. /get_model_info: displays the release of API model
Output example:
{
  "name": "Churn model",
  "version": "v1.0.0"
}
2. /health: displays API status
Output example:

{
  "health": "ok"
}
3. /predict: enables the prediction of Churn variable of an example of customer. 
Input example:
{
  "tenure": 2,
  "no_internet_service": false,
  "internet_service_fiber_optic": false,
  "online_security": false,
  "device_protection": false,
  "contract_month_to_month": true,
  "payment_method_electronic_check": true,
  "paperless_billing": true
}
Output example:
{
  "label": "churner",
  "prediction": 1,
  "probability": 0.53
} 
4. /batch_predict: enables the prediction of Churn variable of a group of customer
Input example: fichier CSV (batch_churn.csv) 
Output example: fichier CSV (predictions-export.csv)

All Input and Output files are stored locally under /data directory 
Finally we can test our api by running:

`$ uvicorn main:api --host 0.0.0.0 --port 8000`

# Docker

Now that we have our web application running, we can use the Dockerfile to create an image for running our web application inside a container

`$ docker build . -t sklearn_fastapi_docker:latest`

And now we can test our application using Docker

`$ docker run -p 8000:8000 sklearn_fastapi_docker`

And then execute below commands as example:
///this command should be executed from churn_project/data directory
curl -X 'POST' \
  'http://127.0.0.1:8000/batch_predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@batch_churn.csv;type=application/vnd.ms-excel'

curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tenure": 2,
  "no_internet_service": false,
  "internet_service_fiber_optic": false,
  "online_security": false,
  "device_protection": false,
  "contract_month_to_month": true,
  "payment_method_electronic_check": true,
  "paperless_billing": true
}'
# Test

The script api_tests.py will be used to test functionnality of API endpoints based on below functions:
1. test_model_info()
2. test_service_health()
3. test_model_predict(): this test is based on an example of input parameter that will be used to predict a known churn value
4. test_batch_predict(): this test is based on an example of input file that will be used to predict a known churn value of a group of customers

Finally, the following command will be used to check test results:
`$  python3 -m pytest api_tests.py`


