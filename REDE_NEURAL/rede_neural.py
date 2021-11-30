from __future__ import absolute_import, division, print_function, unicode_literals
import functools
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

covid_train = pd.read_csv("REDE_NEURAL\info_COVID_train.csv", delimiter=';')
covid_test = pd.read_csv("REDE_NEURAL\info_COVID_test.csv", delimiter=';')

print(f'Shape: {covid_train.shape}')

covid_train = covid_train["contaminados"].values
print("--------------------------")
print(covid_train)
print("--------------------------")
covid_train = covid_train.reshape(-1, 1)
print("--------------------------")
print(covid_train)
print("--------------------------")
