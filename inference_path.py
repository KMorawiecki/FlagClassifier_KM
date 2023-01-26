import os
import sys
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras
import tensorflow as tf

FLAG_WIDTH = 120
FLAG_HEIGHT = 80
FLAGS_DIR = "TestFlags"

model = keras.models.load_model(str(sys.argv[1]))

images = []
for path in os.listdir(FLAGS_DIR):
    flag_path = os.path.join(FLAGS_DIR, path)
    if os.path.isfile(flag_path):
        images.append(keras.preprocessing.image.load_img(flag_path, target_size=(FLAG_HEIGHT, FLAG_WIDTH)))

ind_to_label = {}
for ind, dir_name in enumerate(os.listdir('flags')):
    ind_to_label[ind] = f'{dir_name}'

for img in images:
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = predictions[0]

    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.title(ind_to_label[np.argmax(score)])
    plt.axis("off")
    plt.show()
