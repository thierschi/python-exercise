# ------------------------------------------------------------------------------

# Sheet 12 Exercise 33 - Resubmission

# Niklas Markert - 1611460 / bt709885

# ------------------------------------------------------------------------------

# a)

"""
i) activation (function):
    With the activation parameter we can decide with activation function to use.
    An activation function takes weights (and bias) and input data ("features")
    and yields a number that is given to connected nodes.

ii) optimizer:
    The optimizer computes the update, i.e. the next weights and bias. It does
    so using gradient information (of the loss function).

iii) loss (function):
    The loss function is the function that we want to minimize.

iv) metric(s):
    The metric parameter is used to specify the metric that is used during the
    optimization/learning (for monitoring purposes), i.e. it doesn't influence
    the optimization/learning process.
    All metrics are reported in verbose output.

v) + vi) epochs / batch size:
    The epochs and batch_size parameters decide how many update steps are per-
    formed.
    The batch_size parameter specifies how many samples should be used to compute
    the next update.
    One epoch ends as soon as all samples have been used to compute the update.

    Example: Let the number of training samples be 100, batch_size=32, epochs=2.
    Then the optimizer computes the update of the weights using 32 samples, then
    another two updates using 32 samples each, and another update using the re-
    maining 4 samples. Then one epoch ends. In the next epoch the previously
    computed weights are used as initial values.
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

# Load training and test data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Build the model
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocess the data
train_images_flat = train_images.reshape((60000, 28*28))
test_images_flat = test_images.reshape((10000, 28*28))
train_images_norm = train_images_flat.astype('float32') / 255
test_images_norm = test_images_flat.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Train and run the model
network.fit(train_images_norm, train_labels, epochs=5, batch_size=128)
predictions = network.predict(test_images_norm)

# Evaluate the model
test_loss, test_acc = network.evaluate(test_images_norm, test_labels)

# ------------------------------------------------------------------------------

# b)

max_test_labels = np.argmax(test_labels, axis=1)
max_predictions = np.argmax(predictions, axis=1)

confusion_matrix = metrics.confusion_matrix(max_test_labels, max_predictions)

print("Confusion Matrix:\n" + str(confusion_matrix))


# To see how much ones got falsely recognized as eights we can look into the row
# of actual ones and the column with predicted eights in this case [1, 8]

# No the confusion matrix is not always the same. This is due to the random
# selection of initial weights.

# ------------------------------------------------------------------------------
