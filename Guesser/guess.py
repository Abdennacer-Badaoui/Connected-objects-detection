from Guesser.helpers_guess import *
from Learner.learn import *

# créer la data base à partir d'une capture, selon des cases


def findName(prediction, tagsDictionnary):
    for name, id in tagsDictionnary.keys():
        if id == prediction:
            return name


def guess(path):

    tagsDictionnary = createTagsDictionnary()

    x_guess = build_guess_db(path)
    _, _, prediction_xgboost, proba_xgboost = learn(
        'xgboost', guess=True, x_guess=x_guess)
    _, _, prediction_randomforest, proba_randomforest = learn(
        'xgboost', guess=True, x_guess=x_guess)

    txt_xgboost = f"Prédiction de XGBoost : {findName(prediction_xgboost, tagsDictionnary)} (précision : {int(100*max(proba_xgboost[0]))}%)"
    txt_randomforest = f"Prédiction de RandomForest : {findName(prediction_randomforest, tagsDictionnary)} (précision : {int(100*max(proba_randomforest[0]))}%)"

    return (txt_xgboost, txt_randomforest)
