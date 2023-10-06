import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Carica il dataset MNIST
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocessa i dati
train_images = train_images / 255.0
test_images = test_images / 255.0

# Costruisci il modello di deep learning
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Appiattisce l'immagine 28x28 in un vettore
    layers.Dense(128, activation='relu'),  # Strato nascosto con attivazione ReLU
    layers.Dropout(0.2),  # Dropout per la regolarizzazione
    layers.Dense(10, activation='softmax')  # Strato di output con softmax per classificazione
])

# Compila il modello
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Addestra il modello
model.fit(train_images, train_labels, epochs=5)

# Valuta il modello sul set di test
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")
