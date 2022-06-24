import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

#def load_model():
 #   """
  #  Loads and returns the pretrained model
   # """
    #model = joblib.load("model/model_binary.dat.gz")
    #print("Model loaded")
    #return model


def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction

model = joblib.load("model/model_binary.dat.gz")

def get_model_response(input):
    X = pd.json_normalize(input.__dict__)
    #model=load_model()

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
	
def prepare_data(file):
    #if file is not None:
       # importing the dataset
       file="data/batch_churn.csv"
       df = pd.read_csv(file,sep=';')
       df.head()
       return df
	
def batch_file_predict(input):    
    #model=load_model()
    #Get batch prediction
    prediction = model.predict(input)
    prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
    prediction_df = prediction_df.replace({1:'Yes, this customer is future churner',
                                           0:'No, the customer is non furture churner'})
    return prediction_df
	 
       

