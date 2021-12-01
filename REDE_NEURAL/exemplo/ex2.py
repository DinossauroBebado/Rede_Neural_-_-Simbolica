from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

# convert series to supervised learning
from rede_neural_vis import ploter

epoc = 300
batch = 36


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


# load dataset
dataset_train = read_csv('info_COVID_train.csv',
                         delimiter=';', header=0, index_col=0)
dataset_test = read_csv('info_COVID_test.csv',
                        delimiter=';', header=0, index_col=0)
#dataset = read_csv('pollution.csv', header=0, index_col=0)
values_train = dataset_train.values
values_test = dataset_train.values

# integer encode direction
encoder = LabelEncoder()
values_train[:, 3] = encoder.fit_transform(values_train[:, 3])
values_test[:, 3] = encoder.fit_transform(values_test[:, 3])
# ensure all data is float
values_train = values_train.astype('float32')
values_test = values_test.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train = scaler.fit_transform(values_train)
scaled_test = scaler.fit_transform(values_test)
# specify the number of lag hours
n_hours = 20
n_features = 3
# frame as supervised learning
train = series_to_supervised(scaled_train, n_hours, 1).values
test = series_to_supervised(scaled_test, n_hours, 1).values


# split into input and outputs
n_obs = n_hours * n_features
train_X, train_y = train[:, :n_obs], train[:, -n_features]
test_X, test_y = test[:, :n_obs], test[:, -n_features]
print(train_X.shape, len(train_X), train_y.shape)
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], n_hours, n_features))
test_X = test_X.reshape((test_X.shape[0], n_hours, n_features))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

# design network
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))

model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=epoc, batch_size=batch,
                    validation_data=(test_X, test_y), verbose=2, shuffle=False)
model.save('covid_predict_full.h5')
"""# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()"""

predictions = model.predict(test_X)
predictions = scaler.inverse_transform(predictions)
y_test_scaled = scaler.inverse_transform(test_y.reshape(-1, 1))
"""# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], n_hours*n_features))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, -3:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, -3:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:, 0]"""

rmse = sqrt(mean_squared_error(y_test_scaled, predictions))

ploter(y_test_scaled, predictions, epoc, batch, n_hours, rmse)

# calculate RMSE

print('Test RMSE: %.3f' % rmse)
