# Data processing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np
# Machine Learning Algorithms
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
# Results
from sklearn.metrics import accuracy_score, confusion_matrix


### DATA PROCESSING ###
def import_csv(path):
    return(pd.read_csv(path))


def split(df, trainPercentage):
    features = df.loc[:, df.columns != 'SensorID']
    target = df['SensorID']
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, train_size=trainPercentage, random_state=0)
    return(x_train, y_train, x_test, y_test)

### ENCODING ###


def features_encoder(x_train, x_test, guess=False, x_guess=None):
    sc = StandardScaler()
    x_train_encoded = sc.fit_transform(x_train)
    x_test_encoded = sc.transform(x_test)
    if guess:
        x_guess_encoded = sc.transform(x_guess)
    else:
        x_guess_encoded = None

    return(x_train_encoded, x_test_encoded, x_guess_encoded)


def label_encoder(y_train, y_test):
    le = LabelEncoder()
    values = pd.concat([y_train, y_test]).unique()
    le.fit(values)
    return(le.transform(y_train), le.transform(y_test))


def label_decoder(y_train, y_test, y_guess_encoded):
    le = LabelEncoder()
    values = pd.concat([y_train, y_test]).unique()
    le.fit(values)
    return(le.inverse_transform(y_guess_encoded))


### XGBOOST ###
def model_xgboost(x_train_encoded, y_train_encoded, x_test_encoded, guess=False, x_guess_encoded=None):
    model = XGBClassifier()
    model.fit(x_train_encoded, y_train_encoded)
    y_predict = model.predict(x_test_encoded)
    if guess:
        y_guess = model.predict(x_guess_encoded)
        proba_guess = model.predict_proba(x_guess_encoded)
    else:
        y_guess = None
        proba_guess = None

    return(y_predict, y_guess, proba_guess)

### RANDOM_FOREST_CLASSIFIER ###


def model_randomforest(x_train_encoded, y_train_encoded, x_test_encoded, guess=False, x_guess_encoded=None):
    model = RandomForestClassifier(
        n_estimators=100, criterion='gini', random_state=0)
    model.fit(x_train_encoded, y_train_encoded)
    y_predict = model.predict(x_test_encoded)
    if guess:
        y_guess = model.predict(x_guess_encoded)
        proba_guess = model.predict_proba(x_guess_encoded)
    else:
        y_guess = None
        proba_guess = None

    return(y_predict, y_guess, proba_guess)


### RESULTS ###
def result(y_test_encoded, y_predict):
    R = accuracy_score(y_test_encoded, y_predict)
    mat = confusion_matrix(y_test_encoded, y_predict)
    return(f"Précis à {int(100*R)}%", mat)
