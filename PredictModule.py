import pandas as pd
from joblib import dump,load
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def healthcarePredection():

    df = pd.read_csv('CSVFiles/healthcare-dataset-stroke-data.csv')
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df = df.drop(['id'], axis=1)

    X = df.iloc[:, 0:10]
    y = df.iloc[:, 10]

    X['gender'] = X['gender'].replace('Female', 1)
    X['gender'] = X['gender'].replace('Male', 2)
    X['gender'] = X['gender'].replace('Other', 3)

    X['ever_married'] = X['ever_married'].replace('Yes', 1)
    X['ever_married'] = X['ever_married'].replace('No', 0)

    X['work_type'] = X['work_type'].replace('Private', 1)
    X['work_type'] = X['work_type'].replace('Self-employed', 2)
    X['work_type'] = X['work_type'].replace('children', 3)
    X['work_type'] = X['work_type'].replace('Govt_job', 4)
    X['work_type'] = X['work_type'].replace('Never_worked', 5)

    X['Residence_type'] = X['Residence_type'].replace('Urban', 1)
    X['Residence_type'] = X['Residence_type'].replace('Rural', 2)

    X['smoking_status'] = X['smoking_status'].replace('never smoked', 1)
    X['smoking_status'] = X['smoking_status'].replace('Unknown', 2)
    X['smoking_status'] = X['smoking_status'].replace('formerly smoked', 3)
    X['smoking_status'] = X['smoking_status'].replace('smokes', 4)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    Classifier = GaussianNB()
    ClassifierResult = Classifier.fit(X_train.values, y_train.values)

    # save the classifier
    dump(ClassifierResult, 'ClassifierResult.joblib')


healthcarePredection()
