import pandas as pd
import numpy as np
import joblib
import gzip

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def load_and_prepare_churn_dataset(file):
    # importing the dataset
    df = pd.read_csv(file)
    # drop de customerID qui n'est pas une information utile
    df.drop(columns='customerID', inplace=True)
    # Transformation des labels en données binaires
    df.gender = pd.Series(np.where(df.gender.values == 'Male', 1, 0), df.index)
    df.Partner = pd.Series(np.where(df.Partner.values == 'Yes', 1, 0), df.index)
    df.Dependents = pd.Series(np.where(df.Dependents.values == 'Yes', 1, 0), df.index)
    df.PhoneService = pd.Series(np.where(df.PhoneService.values == 'Yes', 1, 0), df.index)
    df.Churn = pd.Series(np.where(df.Churn.values == 'Yes', 1, 0), df.index)
    df.PaperlessBilling = pd.Series(np.where(df.PaperlessBilling.values == 'Yes', 1, 0), df.index)
    # Correction du type de données de TotalChurn
    # on commence par remplacer les champs vide de la colonne TotalCharges par 0 
    df.TotalCharges = pd.Series(np.where(df.tenure == 0, 0, df.TotalCharges), df.index)
    # On change ensuite le type de la colonne TotalCharges en type numérique float 
    df.TotalCharges = pd.to_numeric(df.TotalCharges, downcast="float")
    return df

df_churn = load_and_prepare_churn_dataset("../data/churn.csv")

# Preselected feature
selected_features = [
    'tenure', 
    'PaperlessBilling',
    'InternetService_Fiber optic',
    'InternetService_No',
    'OnlineSecurity_Yes',
    'DeviceProtection_Yes',
    'Contract_Month-to-month',
    'PaymentMethod_Electronic check'
    ]

# Features encoding
X = pd.get_dummies(df_churn)[selected_features]
y = df_churn.Churn

# Split into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)


# define scaler
scaler = StandardScaler()

# Create an ensemble of 3 models
estimators = []
estimators.append(('logistic', LogisticRegression()))
estimators.append(('cart', DecisionTreeClassifier()))
estimators.append(('gradient_booster', GradientBoostingClassifier(learning_rate= 0.01, n_estimators= 500, min_samples_split= 3, max_features= "log2", max_depth= 3)))

# Create the Ensemble Model
ensemble = VotingClassifier(estimators,voting='soft')

# Make preprocess Pipeline
pipeline = Pipeline([
    ('scaler', scaler),
    ('model', ensemble)
])

pipeline.fit(X_train.values, y_train)

# Test Accuracy
print("Accuracy: %s%%" % str(round(pipeline.score(X_test.values, y_test), 3) * 100))

# Export model
joblib.dump(pipeline, gzip.open('../model/model_binary.dat.gz', "wb"))