# Churn API
Deployment of the Churn ML models using Python's Scikit-Learn + FastAPI + Docker

# Dataset
##Churn  Dataset

The dataset can be found in `data/churn.csv`


### Attribute Information:

    tenure: int
    paperless_billing: int
    internet_service_fiber_optic: int
    no_internet_service: int
    online_security: int
    device_protection: int
    contract_month_to_month: int
    payment_method_electronic_check: int

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

After we have install all the dependencies we can now run the script in code/train.py, this script takes the input data and outputs a trained model and a pipeline for our web service.

`$ python train/train.py`

The model will be saved in the `model` directory

#API endpoints

Finally we can test our api by running:

`$ uvicorn main:api`

# Docker

Now that we have our web application running, we can use the Dockerfile to create an image for running our web application inside a container

`$ docker build . -t sklearn_fastapi_docker`

And now we can test our application using Docker

`$ docker run -p 8000:8000 sklearn_fastapi_docker`

# Test!

Test by using the calls in tests/example_calls.txt from the terminal
