import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Parameters
t = 0.36

# Data Preparation
df = pd.read_csv('weatherAUS.csv', index_col="Date", parse_dates=True)

cat_cols = list(df.dtypes[df.dtypes == "object"].index)
num_cols = list(df.dtypes[df.dtypes != "object"].index)

for col in cat_cols:
    mode_val = df[col].mode()[0] 
    df[col].fillna(mode_val, inplace=True)

for col in num_cols:
    mode_val = df[col].median()
    df[col].fillna(mode_val, inplace=True)

cat_cols.remove("RainTomorrow")

df['RainToday'].replace({'No':0, 'Yes': 1}, inplace = True)
df['RainTomorrow'].replace({'No':0, 'Yes': 1}, inplace = True)

# Splitting

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

# y_train = df_train['RainTomorrow'] 
# y_val = df_val['RainTomorrow'] 
# y_test = df_test['RainTomorrow']

# del df_train['RainTomorrow']
# del df_val['RainTomorrow']
# del df_test['RainTomorrow']

# Training
def train(df_train, y_train, C=1.0):
    dicts = df_train[cat_cols+ num_cols].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[cat_cols+num_cols].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:,1]

    return y_pred

# Training the final model
dv, model = train(df_full_train[cat_cols + num_cols], df_full_train["RainTomorrow"].values, C=1.0)
y_pred = predict(df_test, dv, model)

y_test = df_test["RainTomorrow"].values
auc = roc_auc_score(y_test, y_pred)

print(f"auc={auc}")

# Save the model

with open("model_t.bin", "wb") as f:
    pickle.dump((dv,model), f)

print(f"The model is saved to model_t.bin")