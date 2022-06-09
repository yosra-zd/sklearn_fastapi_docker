import pandas as pd
import joblib

model = joblib.load("model/model_binary.dat.gz")

def predict(X, model):
    return model.predict(X)[0]


def get_model_response(input):    
    X = pd.json_normalize(input.__dict__)
    prediction = predict(X.values, model)
    probability = model.predict_proba(X.values)[0][prediction]
    label = "churner" if prediction == 1 else "non churner"
    return {
        'label': label,
        'prediction': int(prediction),
        'probability': round(probability, 2)
    }