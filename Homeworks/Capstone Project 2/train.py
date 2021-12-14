import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from xgboost import XGBRegressor

# Parameters
rs = 420

# Data Preparation
df = pd.read_csv('heart.csv')

cat_cols = list(df.dtypes[df.dtypes == "object"].index)
num_cols = list(df.dtypes[df.dtypes != "object"].index)
num_cols.remove('HeartDisease')

count_class_1, count_class_0 = df['HeartDisease'].value_counts()

# Divide by class
df_0 = df[df['HeartDisease'] == 0]
df_1 = df[df['HeartDisease'] == 1] 

df_0_more = df_0.sample(count_class_1, replace=True)
df = pd.concat([df_1, df_0_more], axis=0)

# Splitting
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=20)
df_train, df_val = train_test_split(df_full_train, test_size = 0.25, random_state=20)

# y_train = df_train.HeartDisease.values
# y_val = df_val.HeartDisease.values
# y_test = df_test.HeartDisease.values

# df_train = df_train.drop("HeartDisease", axis=1)
# df_val = df_val.drop("HeartDisease", axis=1)
# df_test = df_test.drop("HeartDisease", axis=1)




# val_dict = df_val.to_dict(orient="records")
# X_val = dv.transform(val_dict)

# test_dict = df_test.to_dict(orient="records")
# X_test = dv.transform(test_dict)

# Training
def train(df_train, y_train):
    dv = DictVectorizer(sparse=False)

    train_dict = df_train.to_dict(orient="records")
    X_train = dv.fit_transform(train_dict)

    model = XGBRegressor(n_estimators= 150, colsample_bytree=0.5,
                eta=0.3,
                learning_rate= 0.1,
                max_depth= 4,     
                subsample= 0.6
            )
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[cat_cols+num_cols].to_dict(orient='records')

    X = dv.transform(dicts)
    preds = model.predict(X) >= 0.5

    return preds

# Training the final model
dv, model = train(df_full_train[num_cols], df_full_train["HeartDisease"].values)
y_pred = predict(df_test, dv, model)

y_test = df_test["HeartDisease"].values
auc = roc_auc_score(y_test, y_pred)

print(f"auc={auc}")

# Save the model

with open("model.bin", "wb") as f:
    pickle.dump((dv,model), f)

print(f"The model is saved to model.bin")