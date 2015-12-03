__author__ = 'pdanilov'

from sklearn.ensemble import RandomForestClassifier


def fit_data(features, outputs_df):
    classifier = RandomForestClassifier(min_samples_split=200, njobs=-1)
    outputs = outputs_df['Prediction']
    classifier.fit(features, outputs)
    return classifier


def predict_buy_or_not(classifier, buy_or_not_features):
    return classifier.predict(buy_or_not_features)
