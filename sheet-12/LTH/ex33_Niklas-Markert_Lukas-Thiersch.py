# ------------------------------------------------------------------------------

# Sheet 12 Exercise 33

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# a)

"""
i) In general an activation function acts like a filter (similar as our brain
works) which helps the network to use important and suppress irrelevant data
points.
In this case the activation parameter lets us decide which activation function
should be used (e.g. sigmoid).

ii) An optimizer -as the name states- optimizes the network by adjusting weights
and bias of the network.
Here we can choose between different optimizers, too.

iii) A loss function is the part of the network which tells us how far a prediction
is from the true value.
As with the activation and optimizer we can choose between different loss functions.

iv) Metrics are just additional information that we can choose to be logged in the
verbose log and that don't affect the function of the network.

v) Epochs can be seen as 'one iteration' of the network. The network will use the
weights of the preceding epoch in the next one.

vi) Batch size defines the sample size of one update.
"""

# ------------------------------------------------------------------------------

import tensorflow as tf
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
import numpy as np
from sklearn import metrics

# This is the MNIST code from the lecture condensed into these line until the
# model is trained ignoring outputs

(train_images, train_lables), (test_images, test_lables) = mnist.load_data()
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
train_images_flat = train_images.reshape((60000, 28*28))
test_images_flat = test_images.reshape((10000, 28*28))
train_images_norm = train_images_flat.astype('float32') / 255
test_images_norm = test_images_flat.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
network.fit(train_images_norm, train_lables, epochs=5, batch_size=128)
predictions = network.predict(test_images_norm)

# ------------------------------------------------------------------------------

# b)

max_test_labels = np.argmax(test_lables, axis=1)
max_predictions = np.argmax(predictions, axis=1)

confusion_matrix = metrics.confusion_matrix(max_test_labels, max_predictions)

print("Confusion Matrix:", confusion_matrix)


# To see how much ones got falsely recognized as eights we can look into the row
# of actual ones and the column with predicted eights in this case [1, 8]

# No the confusion matrix is not always the same. This is due to the random
# selection of initial weights.

# ------------------------------------------------------------------------------
