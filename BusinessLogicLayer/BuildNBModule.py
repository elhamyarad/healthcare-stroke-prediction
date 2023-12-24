import pandas as pd
from joblib import dump,load


def healthcarePredection(x):
    clf2 = load('ClassifierResult.joblib')
    Result = clf2.predict([x])
    percentResult = clf2.predict_proba([x])

    return Result, percentResult
