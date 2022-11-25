from Learner.helpers_learn import *


def learn(model, guess=False, x_guess=None):
    trainingDf = import_csv("Learner/TrainingDB/trainingDB_reel.csv")
    x_train, y_train, x_test, y_test = split(trainingDf, 0.8)
    x_train_encoded, x_test_encoded, x_guess_encoded = features_encoder(
        x_train, x_test, guess, x_guess)
    y_train_encoded, y_test_encoded = label_encoder(y_train, y_test)
    if model == 'randomforest':
        y_predict_encoded, y_guess_encoded, proba_guess = model_randomforest(x_train_encoded, y_train_encoded,
                                                                             x_test_encoded, guess, x_guess_encoded)
    elif model == 'xgboost':
        y_predict_encoded, y_guess_encoded, proba_guess = model_xgboost(x_train_encoded, y_train_encoded,
                                                                        x_test_encoded, guess, x_guess_encoded)
    else:
        raise Error('machine learning algorithm unknown or not implemented')

    txt, mat = result(y_test_encoded, y_predict_encoded)

    if guess:
        y_guess = int(label_decoder(y_train, y_test, y_guess_encoded))
    else:
        y_guess = None

    return(txt, mat, y_guess, proba_guess)
