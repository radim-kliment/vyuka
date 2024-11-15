import pandas as pd
import keras
import tensorflow as tf
from keras import layers
from sklearn.model_selection import train_test_split
# Load the data
data = pd.read_csv('Sleep_Efficiency.csv')

# ID,Age,Gender,Bedtime,Wakeup time,Sleep duration,Sleep efficiency,REM sleep percentage,Deep sleep percentage,Light sleep percentage,Awakenings,Caffeine consumption,Alcohol consumption,Smoking status,Exercise frequency

# pyenv install 3.11
# pyenv global 3.11
# rm -rf env
# python -m venv env
# source env/bin/activate
# pip install pandas keras tensorflow
# pip install scikit-learn

data = data.drop(['ID', 'Bedtime', 'Wakeup time'], axis=1)

data['Smoking status']  = pd.Categorical(data['Smoking status'])
data['Smoking status'] = data['Smoking status'].cat.codes
data['Gender'] = pd.Categorical(data['Gender'])
data['Gender'] = data['Gender'].cat.codes

data = data.astype('float32')

data = data.dropna()

x = data.drop('Sleep efficiency', axis=1)
y = data['Sleep efficiency']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = keras.Sequential(
    [
        layers.Dense(X_train.shape[1], activation="relu"),
        layers.Dense(X_train.shape[1]//2, activation="relu"),
        layers.Dense(X_train.shape[1]//3, activation="relu"),
        layers.Dense(1, activation="relu"),
    ]
)

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=50, validation_split=0.17)

score = model.evaluate(X_test, y_test)

converter = tf.lite.TFLiteConverter.from_keras_model(model) 
tflite_model = converter.convert()

with open('converted_model.tflite', 'wb') as f:     
    f.write(tflite_model)

