import os, warnings

# Imports
import os, warnings
import matplotlib.pyplot as plt
from matplotlib import gridspec


import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')
warnings.filterwarnings("ignore") # to clean up output cells

# Reproducability
def set_seed(seed=31415):
    np.random.seed(seed)
    tf.random.set_seed(seed)
set_seed()

# Load training and validation sets
ds_train_ = image_dataset_from_directory(
    r'C:\Users\pc\Desktop\AI and ML\ML\Datasets\OpenCV\Car-Truck\car-truck\train',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=True,
)
ds_valid_ = image_dataset_from_directory(
    r'C:\Users\pc\Desktop\AI and ML\ML\Datasets\OpenCV\Car-Truck\car-truck\valid',
    labels='inferred',
    label_mode='binary',
    image_size=[128, 128],
    interpolation='nearest',
    batch_size=64,
    shuffle=False,
)

# Data Pipeline

def convert_to_float(image, label):
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    return image, label

AUTOTUNE = tf.data.experimental.AUTOTUNE
ds_train = (
    ds_train_
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)
ds_valid = (
    ds_valid_
    .map(convert_to_float)
    .cache()
    .prefetch(buffer_size=AUTOTUNE)
)



model = keras.Sequential([
    layers.Conv2D(filters=32, kernel_size=3, activation='relu',
                  padding='same', input_shape=[128,128,3]),
    layers.MaxPool2D(),

    layers.Conv2D(filters=32, kernel_size=3,
                  activation='relu', padding='same'),
    layers.MaxPool2D(),
    layers.Conv2D(filters=32, kernel_size=3,
                  activation='relu', padding='same'),
    layers.MaxPool2D(),

    layers.Flatten(),
    layers.Dense(6, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(6, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid'),

])

print(model.summary())

# model.compile(optimizer='Adam',
#               loss='binary_crossentropy',
#               metrics=['binary_accuracy'])
#
# history = model.fit(
#     ds_train,
#     validation_data=ds_valid,
#     epochs=50,
# )
#
# import pandas as pd
# history_frame = pd.DataFrame(history.history)
# print(history_frame.loc[:, ['loss', 'val_loss']].plot())
# print(history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot())
# plt.show()