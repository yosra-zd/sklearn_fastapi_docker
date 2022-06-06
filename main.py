import uvicorn
from fastapi import FastAPI

# Third party imports
from pydantic import BaseModel, Field
from typing import List

from ms.functions import get_model_response

model_name = "Churn model"
version = "v1.0.0"

api = FastAPI()

# Input for data validation
class Input(BaseModel):
    tenure: int
    paperless_billing: int
    internet_service_fiber_optic: int
    no_internet_service: int
    online_security: int
    device_protection: int
    contract_month_to_month: int
    payment_method_electronic_check: int

    

    class Config:
        schema_extra = {
            'tenure': 29,
            'paperless_billing': 1,
            'internet_service_fiber_optic': 0,
            'no_internet_service': 1,
            'online_security': 0,
            'device_protection': 0,
            'contract_month_to_month': 0,
            'payment_method_electronic_check': 1
        }


# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int
    probability: float


@api.get('/')
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@api.get('/health')
async def service_health():
    """Return service health"""
    return {
        "health": "ok"
    }


@api.post('/predict', response_model=Output)
async def model_predict(input: Input):
    """Predict with input"""
    response = get_model_response(input)
    return response