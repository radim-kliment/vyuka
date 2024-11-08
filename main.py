import pandas as pd
import keras
import tensorflow as tf
from keras import layers

# Load the data
data = pd.read_csv('Sleep_Efficiency.csv')

# ID,Age,Gender,Bedtime,Wakeup time,Sleep duration,Sleep efficiency,REM sleep percentage,Deep sleep percentage,Light sleep percentage,Awakenings,Caffeine consumption,Alcohol consumption,Smoking status,Exercise frequency

data = data.drop(['ID', 'Bedtime', 'Wakeup time'], axis=1)

data['Smoking status']  = pd.Categorical(data['Smoking status'])
data['Smoking status'] = data['Smoking status'].cat.codes
data['Gender'] = pd.Categorical(data['Gender'])
data['Gender'] = data['Gender'].cat.codes

x = data.drop('Sleep efficiency', axis=1)
y = data['Sleep efficiency']

model = keras.Sequential(
    [
        layers.Dense(x.shape[1], activation="relu"),
        layers.Dense(x.shape[1]//2, activation="relu"),
        layers.Dense(x.shape[1]//3, activation="relu"),
        layers.Dense(1, activation="relu"),
    ]
)

print(data.head()) 

