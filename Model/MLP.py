import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
from keras.optimizers import Adam
from keras.regularizers import L1, L2


def visualize_data(data):
    images_to_show = 36
    per_row = 12
    fig = plt.figure(figsize=(20, 5))
    for i in range(images_to_show):
        pos = (i // per_row, ((i % per_row) + per_row) % per_row)
        ax = plt.subplot2grid((int(images_to_show / per_row), per_row),
                              pos, xticks=[], yticks=[])
        ax.imshow(np.squeeze(data.x_train[i]))
    plt.show()


def preprocess(train_ds, val_ds, categories):
    train_x = np.array([]).reshape((0, 80, 120, 3))
    train_y = np.array([]).reshape(0, )
    val_x = np.array([]).reshape((0, 80, 120, 3))
    val_y = np.array([]).reshape(0, )

    for x_t, y_t in train_ds:
        train_x = np.concatenate((train_x, x_t), axis=0)
        train_y = np.concatenate((train_y, y_t), axis=0)
    train_x = train_x.astype("float32") / 255
    train_y = to_categorical(train_y, categories)
    for x_v, y_v in val_ds:
        val_x = np.concatenate((val_x, x_v), axis=0)
        val_y = np.concatenate((val_y, y_v), axis=0)
    val_x = val_x.astype("float32") / 255
    val_y = to_categorical(val_y, categories)

    return {"x_train": train_x,
            "y_train": train_y,
            "x_test": val_x[:int(len(val_x)/2)],
            "y_test": val_y[:int(len(val_y)/2)],
            "x_val": val_x[int(len(val_x)/2):],
            "y_val": val_y[int(len(val_y)/2):]}


def build_mlp(categories, learning_rate):
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(512,
                    activation="relu"))
    model.add(Dense(256,
                    activation="relu"))
    model.add(Dense(categories,
                    activity_regularizer=L1(0.01),
                    activation="softmax"))
    # Compile the model
    model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=learning_rate),
                  metrics=["accuracy"])
    return model
