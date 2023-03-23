"""
Sprint 2 - Bayes Project
Efe Comu
"""

## Practice Problems
#
# 1) "watch anime now"
# watch --> P(word / spam) = 0.09, P(word / not spam) = 0.055
# anime --> P(word / spam) = 0.09, P(word / not spam) = 0.055
# now --> P(word / spam) = 0.09, P(word / not spam) = 0.055
## Answer: (0.09 ^ 3) > (0.055 ^ 3) --> more likely to be SPAM.
#
# 2) "takeout and anime at my house"
# takeout --> P(word / spam) = 0.05, P(word / not spam) = 0.11
# and --> P(word / spam) = 0.05, P(word / not spam) = 0.055
# anime --> P(word / spam) = 0.09, P(word / not spam) = 0.055
# my --> P(word / spam) = 0.05, P(word / not spam) = 0.055
# house --> P(word / spam) = 0.09, P(word / not spam) = 0.11
## Answer: 10.13 * 10 ^ -7 < 20.13 * 10 ^ -7, therefore more likely to be NOT SPAM
#
# 3) "sell me your anime collection"
# sell --> P(word / spam) = 0.09, P(word / not spam) = 0.055
# me --> P(word / spam) = 0.05, P(word / not spam) = 0.055
# your --> P(word / spam) = 0.09, P(word / not spam) = 0.055
# anime --> P(word / spam) = 0.09, P(word / not spam) = 0.055
# collection --> P(word / spam) = 0.05, P(word / not spam) = 0.055
## Answer: The product of P(word / spam) is clearly higher, most likely to be SPAM

# ---------------------------------------------
# Code
"""
Example spam filtering model using a naive Bayesian classifier.

The spam.csv dataset is from Kaggle.
"""

#--- Imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np
import pandas as pd

#--- Load spam.csv as a Pandas dataframe
df = pd.read_csv('spam.csv', header=0, encoding='latin1')
print(df)

#--- Split into training and testing sets, 70-30 ratio
#
# df['message'] is the column of text message contents
# df['label'] is the column of labels for each message, either 'spam' or 'ham'
#
# X_train is the set of training messages
# y_train is the set of correct labels for the training messages
# X_test is the set of testing messages
# y_test is the set of correct labels for the testing messages

X_train, X_test, y_train, y_test = train_test_split(df['message'],
                                                    df['label'],
                                                    test_size=0.30)

#--- Build a Pipeline that implements the classifier
#
# 1. CountVectorizer turns input text into counts of words
# 2. MultinomialNB is the multinomial naive Bayes classifier

text_clf = Pipeline([
  ('vect', CountVectorizer()),
  ('clf', MultinomialNB()),
])

#--- Fit the model to the training data
text_clf.fit(X_train, y_train)

#--- Use the trained model to predict classes on the test set
predicted = text_clf.predict(X_test)

#--- Testing accuracy
print(np.mean(predicted == y_test))

#--- Print more detailed assessment of the model's performance
print(
  metrics.classification_report(y_test,
                                predicted,
                                target_names=['spam', 'ham']))
