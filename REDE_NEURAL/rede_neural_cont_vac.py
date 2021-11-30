from __future__ import absolute_import, division, print_function, unicode_literals
import functools
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout

import matplotlib.pyplot as plt

from rede_neural_vis import ploter

epoc = 300
batch = 32
dias = 20


def create_dataset(df):
    x = []
    y = []
    print(df)
    print("-------DB---------------------------------------------")
    for i in range(dias, df.shape[0]):
        x.append(df[i-dias:i, 0].extend[df[i][1], df[i][2], df[i][3]])
        y.append(df[i, 0])
    x = np.array(x)
    y = np.array(y)
    return x, y


covid_train_csv = pd.read_csv(
    "REDE_NEURAL\info_COVID_train.csv", delimiter=';')
covid_test_csv = pd.read_csv("REDE_NEURAL\info_COVID_test.csv", delimiter=';')

print(f'Shape: {covid_train_csv.shape}')

covid_train_csv.drop('data', inplace=True, axis=1)
covid_test_csv.drop('data', inplace=True, axis=1)

covid_train = covid_train_csv.values

covid_test = covid_test_csv.values


covid_train = covid_train.reshape(-1, 4)
covid_test = covid_test.reshape(-1, 4)


scaler = MinMaxScaler(feature_range=(0, 1))

dataset_train = scaler.fit_transform(covid_train)
dataset_test = scaler.transform(covid_test)


x_train, y_train = create_dataset(dataset_train)
x_test, y_test = create_dataset(dataset_test)
print("-------DB---------------------------------------------")
print(x_train)
print("-------DB---------------------------------------------")
"""x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

print(x_test)"""
'''
model = Sequential()
model.add(LSTM(units=96, return_sequences=True,
          input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=96, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96))
model.add(Dropout(0.2))
model.add(Dense(units=1))

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, epochs=epoc, batch_size=batch)
model.save('covid_predict.h5')

# model = load_model('covid_predict.h5')

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))


ploter(y_test_scaled, predictions, epoc, batch, dias)
'''
