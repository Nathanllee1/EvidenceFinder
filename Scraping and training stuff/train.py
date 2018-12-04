from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
import pandas as pd

import re

df = pd.read_csv('alldata.csv')

print(df[0])

#for themequote in df["themequote"]:
    #themequote = re.sub(r'[^a-zA-Z0-9]', '', themequote)



'''
#select training vs test data
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .80
train, test = df[df['is_train']==True], df[df['is_train']==False]

print('Number of quotes in the training data:', len(train))
print('Number of quotes in the test data:',len(test))

features = df.columns[:4]

y = pd.factorize(train['Boolean'])[0]
print(y)


corpus = train['themequote']
vectorizer = TfidfVectorizer(lowercase=True, stop_words='english', strip_accents='ascii')
x = vectorizer.fit_transform(corpus)

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], y)
'''
