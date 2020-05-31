import pandas as pd 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

import numpy as np

print('Reading Files...');
data = pd.read_csv("train.csv", usecols=["text", "class"]);
# unknown_class = pd.read_csv("test.csv", usecols=["text", "class"]);
# unknown_class = unknown_class[unknown_class['text'].apply(type) == str]
# print(unknown_class.info())
# print(test.info())

print('Split Data for Validation...');
train, test = train_test_split(data, test_size=0.33)
# print(train.info())
# print(test.info())

text_clf = Pipeline([
	('vect', CountVectorizer()),
	('tfidf', TfidfTransformer()),
	('clf', MultinomialNB()),
]);

print('Fitting Bayes...');
text_clf.fit(train['text'], train['class']);

print('Predicting Bayes...');
train_prediction = text_clf.predict(test['text']);
score = metrics.accuracy_score(test['class'], train_prediction)
print("accuracy:   %0.3f" % score)
print(metrics.classification_report(test['class'], train_prediction))

# print('happy predictions');
# print(np.count_nonzero(train_prediction == 'happy'));

# print('sad predictions');
# print(np.count_nonzero(train_prediction == 'sad'));

# print('hope predictions');
# print(np.count_nonzero(train_prediction == 'hope'));

# print('angry predictions');
# print(np.count_nonzero(train_prediction == 'angry'));
