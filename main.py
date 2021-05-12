# %% imports

import numpy as np
import pandas as pd
import seaborn as sns
from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# %% data

data = pd.read_csv("data/heart.csv")
o2s = pd.read_csv("data/o2Saturation.csv")


# %% rerational anylisis

profile = ProfileReport(data, title="Heart-Attack")
profile.to_file("your_report.html")

# %% summary

data.describe()


# %% info

data.info()


# %% corelation table
#data.corr(method="spearman")
data.corr(method="pearson")


# %% color palette

sns.set_palette("Set2")


# %% gender ratio

ax=sns.countplot(x='sex', data=data)
ax.set(xlabel='1=>Male, 0=>Female',ylabel='Counts',title='Gender Ratio')

# %% exang
'''
    male = 1
    exercise induced angina have a high posibility in Male then female.
'''
ax=sns.countplot(x='exng',hue='sex',data=data)

# %% chest pain

'''
    0: Typical Angina
    1: Atypical Angina
    2: Non-Anginal Pain
    3: Asymptomatic
'''
ax=sns.countplot(x='cp', data=data)

# %% effect of chol to cp

data = data.replace({'cp': {0:'Typical Angina' ,1:'Atypical Angina',2:'Non-Anginal Pain',3:'Asymptomatic'}})

ax=sns.histplot(data=data, x="chol", bins=5,binwidth=30, kde=True,hue='cp')
ax.set(title='How cholesterol affects chest pain type')

# %% chol vs age

'''
    since age and chol have a +ve co-relation as the age inc. chol tends to inc.
'''
sns.lineplot(data=data,x='age',y='chol')


# %% caa relation ship with output

sns.violinplot(x='caa',y='output', data =data)

# %%
sns.violinplot(x='fbs',y='trtbps', data =data)

# %%

'''
    How max heart rate affects the probability of having heart attack?
    There's positive correlation co-efficient of 0.421741 ("pearson") between them, so we can assume that having a higher heart rate is a factor contributing to heart attack.
'''
sns.lineplot(y='thalachh',x='output', data=data)


# %%

'''
    acc = 0.6842105263157895 or 68.42%
'''
train_data = data.drop(['output'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
        train_data, data['output'], random_state=0)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
prediction = knn.predict(X_test)

print(np.mean(prediction == y_test))

