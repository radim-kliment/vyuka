
import pandas as pd
import tensorflow as tf
import numpy as np

interpreter = tf.lite.Interpreter(model_path='converted_model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

predictdata = pd.DataFrame({
    'Age': [20],
    'Gender': [1],
    'Sleep duration': [8],
    'REM sleep percentage': [20],
    'Deep sleep percentage': [20],
    'Light sleep percentage': [60],
    'Awakenings': [1],
    'Caffeine consumption': [1],
    'Alcohol consumption': [1],
    'Smoking status': [1],
    'Exercise frequency': [3]
})

predictdata = predictdata.astype('float32')

input_data = np.array(predictdata.values, dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)

