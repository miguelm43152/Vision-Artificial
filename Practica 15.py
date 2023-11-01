# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:48:20 2023

@author: Javier
"""

# Importar las bibliotecas necesarias
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset Fashion MNIST
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Definir las clases de ropa en el dataset
class_names = ['T-shirt/top', 'Pantalón', 'Pullover', 'Vestido', 'Abrigo',
               'Sandalia', 'Camisa', 'Zapatilla deportiva', 'Bolso', 'Botín']

# Preprocesar los datos
train_images = train_images / 255.0
test_images = test_images / 255.0

# Crear el modelo de la red neuronal
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=10)

# Evaluar la precisión del modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\nPrecisión en el conjunto de prueba:', test_acc)

# Hacer predicciones con el modelo entrenado
predictions = model.predict(test_images)

# Mostrar una imagen de ejemplo y su predicción
plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

# Imprimir la etiqueta predicha
predicted_label = np.argmax(predictions[0])
print('Etiqueta predicha:', class_names[predicted_label])