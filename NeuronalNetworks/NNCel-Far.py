# Red Neuronal para transformar celsius a farenheit

import tensorflow as tf
import numpy as np
# import matplotlib.pyplot as plt

celsius = np.array([-40,-10, 0, 8, 15, 22, 38], dtype=float)
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

layer = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer])
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.05),
    loss='mean_squared_error'
)
print('Comenzando Entrenamiento')
history = model.fit(celsius, farenheit, epochs=1000, verbose=False)
print('Modelo Entrenado')

# plt.xlabel('# Epoca')
# plt.ylabel('Pérdida')
# plt.plot(history.history['loss'])

print('Prediccion')
result = model.predict([100.0])
print(f'El resultado es {result} grados farenheit')

