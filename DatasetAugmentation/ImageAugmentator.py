import tensorflow as tf
import os
from tensorflow.keras import layers
from PIL import Image


class ImageAugemtator:
    def __init__(self, dataset_path, img_width, img_height):
        self.dataset_path = dataset_path
        self.img_width = img_width
        self.img_height = img_height

    def create_image_variations(self):
        for path in os.listdir(self.dataset_path):
            dir_path = os.path.join(self.dataset_path, path)
            img_path = os.path.join(dir_path, os.listdir(dir_path)[0])
            if os.path.isfile(img_path):
                img = Image.open(img_path)
                img_name = os.path.basename(path).split('/')[-1].split('.')[0]
                proc_img = self.generate_processing_image(img)

                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_resized0.jpg'),
                                                      self.generate_resized_img(proc_img, 30, 10))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_resized1.jpg'),
                                                      self.generate_resized_img(proc_img, 40, 20))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_resized2.jpg'),
                                                      self.generate_resized_img(proc_img, 50, 10))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_resized3.jpg'),
                                                      self.generate_resized_img(proc_img, 70, 20))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_resized4.jpg'),
                                                      self.generate_resized_img(proc_img, 90, 10))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_contrast0.jpg'),
                                                      self.generate_random_contrast_img(proc_img, (0.3, 0.7)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_contrast1.jpg'),
                                                      self.generate_random_contrast_img(proc_img, (0.3, 0.7)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_contrast2.jpg'),
                                                      self.generate_random_contrast_img(proc_img, (0.3, 0.7)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_contrast3.jpg'),
                                                      self.generate_random_contrast_img(proc_img, (0.3, 0.7)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_contrast4.jpg'),
                                                      self.generate_random_contrast_img(proc_img, (0.3, 0.7)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_crop0.jpg'),
                                                      self.generate_random_crop_img(proc_img, 70, 100))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_crop1.jpg'),
                                                      self.generate_random_crop_img(proc_img, 75, 95))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_crop2.jpg'),
                                                      self.generate_random_crop_img(proc_img, 65, 90))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_zoom0.jpg'),
                                                      self.generate_random_zoom_img(proc_img,
                                                                                    (-0.2, 0.3),
                                                                                    (-0.2, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_zoom1.jpg'),
                                                      self.generate_random_zoom_img(proc_img,
                                                                                    (-0.2, 0.3),
                                                                                    (-0.2, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_zoom2.jpg'),
                                                      self.generate_random_zoom_img(proc_img,
                                                                                    (-0.2, 0.3),
                                                                                    (-0.2, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_zoom3.jpg'),
                                                      self.generate_random_zoom_img(proc_img,
                                                                                    (-0.2, 0.3),
                                                                                    (-0.2, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_zoom4.jpg'),
                                                      self.generate_random_zoom_img(proc_img,
                                                                                    (-0.2, 0.3),
                                                                                    (-0.2, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_bright0.jpg'),
                                                      self.generate_random_brightness_img(proc_img, (-0.3, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_bright1.jpg'),
                                                      self.generate_random_brightness_img(proc_img, (-0.3, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_bright2.jpg'),
                                                      self.generate_random_brightness_img(proc_img, (-0.3, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_bright3.jpg'),
                                                      self.generate_random_brightness_img(proc_img, (-0.3, 0.3)))
                tf.keras.preprocessing.image.save_img(os.path.join(dir_path, f'{img_name}_bright4.jpg'),
                                                      self.generate_random_brightness_img(proc_img, (-0.3, 0.3)))

    def generate_processing_image(self, image):
        augmentation_model = tf.keras.Sequential([
            layers.Resizing(self.img_height, self.img_width)
        ])
        return augmentation_model(tf.convert_to_tensor(image))

    def generate_resized_img(self, image, height_pad, width_pad):
        augmentation_model = tf.keras.Sequential([
                                layers.Resizing(self.img_height + height_pad, self.img_width + width_pad)
                            ])
        return augmentation_model(tf.convert_to_tensor(image))

    def generate_random_contrast_img(self, image, factor):
        augmentation_model = tf.keras.layers.RandomContrast(factor)
        return augmentation_model(tf.convert_to_tensor(image))

    def generate_random_crop_img(self, image, height_crop, width_crop):
        augmentation_model = tf.keras.layers.RandomCrop(height_crop, width_crop)
        return augmentation_model(tf.convert_to_tensor(image))

    def generate_random_zoom_img(self, image, height_factor, width_factor):
        augmentation_model = tf.keras.layers.RandomZoom(
                                height_factor,
                                width_factor,
                                fill_mode='reflect',
                                interpolation='bilinear',
                                seed=None,
                                fill_value=0.0
                            )
        return augmentation_model(tf.convert_to_tensor(image))

    def generate_random_brightness_img(self, image, factor):
        augmentation_model = tf.keras.layers.RandomBrightness(factor, value_range=(0, 255))
        return augmentation_model(tf.convert_to_tensor(image))
