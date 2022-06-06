import pandas as pd
import joblib

model = joblib.load("model/model_binary.dat.gz")

def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction


def get_model_response(input):    
    X = pd.json_normalize(input.__dict__)
    prediction = predict(X.values, model)
    probability = model.predict_proba(X.values)[0][prediction]
    if prediction == 1:
        label = "churner"
    else:
        label = "non churner"
    return {
        'label': label,
        'prediction': int(prediction),
        'probability': round(probability, 2)
    }
    
    
    