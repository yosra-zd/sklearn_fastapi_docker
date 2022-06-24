import pandas as pd
import joblib
<<<<<<< HEAD

model = joblib.load("model/model_binary.dat.gz")
=======
from sklearn.preprocessing import MinMaxScaler

#def load_model():
 #   """
  #  Loads and returns the pretrained model
   # """
    #model = joblib.load("model/model_binary.dat.gz")
    #print("Model loaded")
    #return model

>>>>>>> yosradev

def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction
<<<<<<< HEAD


def get_model_response(input):    
    X = pd.json_normalize(input.__dict__)
=======
model = joblib.load("model/model_binary.dat.gz")

def get_model_response(input):
    X = pd.json_normalize(input.__dict__)
    #model=load_model()
>>>>>>> yosradev
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
<<<<<<< HEAD
    
    
    
=======
	
def prepare_data(file):
    if uploaded_file is not None:
       # importing the dataset
       df = pd.read_csv(file)
       # drop de customerID qui n'est pas une information utile
       df.drop(columns='customerID', inplace=True)
       # Transformation des labels en données binaires
       df.gender = pd.Series(np.where(df.gender.values == 'Male', 1, 0), df.index)
       df.Partner = pd.Series(np.where(df.Partner.values == 'Yes', 1, 0), df.index)
       df.Dependents = pd.Series(np.where(df.Dependents.values == 'Yes', 1, 0), df.index)
       df.PhoneService = pd.Series(np.where(df.PhoneService.values == 'Yes', 1, 0), df.index)
       df.SeniorCitizen = pd.Series(np.where(df.SeniorCitizen.values == 'Yes', 1, 0), df.index)
       df.PaperlessBilling = pd.Series(np.where(df.PaperlessBilling.values == 'Yes', 1, 0), df.index)
       # Correction du type de données de TotalChurn
       # on commence par remplacer les champs vide de la colonne TotalCharges par 0 
       df.TotalCharges = pd.Series(np.where(df.tenure == 0, 0, df.TotalCharges), df.index)
       # On change ensuite le type de la colonne TotalCharges en type numérique float 
       # df.TotalCharges = pd.to_numeric(df.TotalCharges, errors='coerce')
       df.TotalCharges = pd.to_numeric(df.TotalCharges, downcast="float")
	   #feature scaling
       sc = MinMaxScaler()
       df['tenure'] = sc.fit_transform(df[['tenure']])
       df['MonthlyCharges'] = sc.fit_transform(df[['MonthlyCharges']])
       df['TotalCharges'] = sc.fit_transform(df[['TotalCharges']])
       df = pd.get_dummies(df)
       return df
	
def batch_file_predict(input):    
    #model=load_model()
    #Get batch prediction
    prediction = model.predict(input)
    prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
    prediction_df = prediction_df.replace({1:'Yes, this customer is future churner',
                                           0:'No, the customer is non furture churner'})
    return prediction_df
	 
       
>>>>>>> yosradev
