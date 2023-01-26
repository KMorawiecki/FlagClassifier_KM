import tensorflow as tf
import numpy as np

from Model.MLP import build_mlp, preprocess


num_epochs = 6
batch_size = 16
learning_rate = .0001
seed_value = 200

tf.random.set_seed(seed_value)

train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
    "flags",
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=(80, 120),
    batch_size=16,
    shuffle=True
)

x_train = np.concatenate([x for x, y in train_ds], axis=0)
num_labels = len(train_ds.class_names)
processed_data = preprocess(train_ds, val_ds, num_labels)

mlp = build_mlp(num_labels, learning_rate)

mlp.fit(processed_data["x_train"],
        processed_data["y_train"],
        batch_size=batch_size,
        epochs=num_epochs,
        validation_data=(processed_data["x_val"], processed_data["y_val"]),
        shuffle=True)

mlp.save('mlp_new')

scores = mlp.evaluate(processed_data["x_test"], processed_data["y_test"], verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
