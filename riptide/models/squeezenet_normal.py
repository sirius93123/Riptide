import tensorflow as tf
import tensorflow.keras.layers as nn

bnmomemtum=0.9

class SqueezeNet(tf.keras.Model):
    def __init__(self, classes=1000):
        super(SqueezeNet, self).__init__()
        self.classes = classes

        self.c0 = tf.keras.layers.Conv2D(kernel_size=7, strides=2, filters=96, padding='same', use_bias=True, activation='relu')
        self.b0 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.mp0 = tf.keras.layers.MaxPooling2D(pool_size=2)

        # Fire 1
        self.f1c1 = tf.keras.layers.Conv2D(filters=32, kernel_size=1, activation='relu', padding='same')
        self.f1b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f1c2 = tf.keras.layers.Conv2D(filters=64, kernel_size=1, activation='relu', padding='same')
        self.f1b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f1c3 = tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same')
        self.f1b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f1concat = tf.keras.layers.Concatenate(axis=-1)

        # Fire 2
        self.f2c1 = tf.keras.layers.Conv2D(filters=32, kernel_size=1, activation='relu', padding='same')
        self.f2b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f2c2 = tf.keras.layers.Conv2D(filters=64, kernel_size=1, activation='relu', padding='same')
        self.f2b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f2c3 = tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same')
        self.f2b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f2concat = tf.keras.layers.Concatenate(axis=-1)

        # Fire 3
        self.f3c1 = tf.keras.layers.Conv2D(filters=32, kernel_size=1, activation='relu', padding='same')
        self.f3b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f3c2 = tf.keras.layers.Conv2D(filters=128, kernel_size=1, activation='relu', padding='same')
        self.f3b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f3c3 = tf.keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same')
        self.f3b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f3concat = tf.keras.layers.Concatenate(axis=-1)

        self.mp3 = tf.keras.layers.MaxPooling2D(pool_size=2)

        # Fire 4
        self.f4c1 = tf.keras.layers.Conv2D(filters=32, kernel_size=1, activation='relu', padding='same')
        self.f4b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f4c2 = tf.keras.layers.Conv2D(filters=128, kernel_size=1, activation='relu', padding='same')
        self.f4b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f4c3 = tf.keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same')
        self.f4b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f4concat = tf.keras.layers.Concatenate(axis=-1)

        # Fire 5
        self.f5c1 = tf.keras.layers.Conv2D(filters=64, kernel_size=1, activation='relu', padding='same')
        self.f5b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f5c2 = tf.keras.layers.Conv2D(filters=192, kernel_size=1, activation='relu', padding='same')
        self.f5b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f5c3 = tf.keras.layers.Conv2D(filters=192, kernel_size=3, activation='relu', padding='same')
        self.f5b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f5concat = tf.keras.layers.Concatenate(axis=-1)

        # Fire 6
        self.f6c1 = tf.keras.layers.Conv2D(filters=64, kernel_size=1, activation='relu', padding='same')
        self.f6b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f6c2 = tf.keras.layers.Conv2D(filters=192, kernel_size=1, activation='relu', padding='same')
        self.f6b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f6c3 = tf.keras.layers.Conv2D(filters=192, kernel_size=3, activation='relu', padding='same')
        self.f6b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f6concat = tf.keras.layers.Concatenate(axis=-1)

        # Fire 7
        self.f7c1 = tf.keras.layers.Conv2D(filters=64, kernel_size=1, activation='relu', padding='same')
        self.f7b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f7c2 = tf.keras.layers.Conv2D(filters=256, kernel_size=1, activation='relu', padding='same')
        self.f7b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f7c3 = tf.keras.layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same')
        self.f7b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f7concat = tf.keras.layers.Concatenate(axis=-1)

        self.mp7 = tf.keras.layers.MaxPooling2D(pool_size=2)

        # Fire 8
        self.f8c1 = tf.keras.layers.Conv2D(filters=64, kernel_size=1, activation='relu', padding='same')
        self.f8b1 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f8c2 = tf.keras.layers.Conv2D(filters=256, kernel_size=1, activation='relu', padding='same')
        self.f8b2 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f8c3 = tf.keras.layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same')
        self.f8b3 = tf.keras.layers.BatchNormalization(momentum=bnmomemtum)
        self.f8concat = tf.keras.layers.Concatenate(axis=-1)

        # Output
        self.avgpool = tf.keras.layers.GlobalAveragePooling2D()
        self.classifier = tf.keras.layers.Dense(1000, activation='softmax')

    def call(self, x, training=None):
        y = self.c0(x)
        y = self.b0(y, training=training)
        y = self.mp0(y)

        # Fire 1
        y = self.f1c1(y)
        y = self.f1b1(y, training=training)
        y1x = self.f1c2(y)
        y1x = self.f1b2(y1x, training=training)
        y3x = self.f1c3(y)
        y3x = self.f1b3(y3x, training=training)
        y = self.f1concat([y1x, y3x])

        # Fire 2
        y = self.f2c1(y)
        y = self.f2b1(y, training=training)
        y1x = self.f2c2(y)
        y1x = self.f2b2(y1x, training=training)
        y3x = self.f2c3(y)
        y3x = self.f2b3(y3x, training=training)
        y = self.f2concat([y1x, y3x])

        # Fire 3
        y = self.f3c1(y)
        y = self.f3b1(y, training=training)
        y1x = self.f3c2(y)
        y1x = self.f3b2(y1x, training=training)
        y3x = self.f3c3(y)
        y3x = self.f3b3(y3x, training=training)
        y = self.f3concat([y1x, y3x])

        y = self.mp3(y)

        # Fire 4
        y = self.f4c1(y)
        y = self.f4b1(y, training=training)
        y1x = self.f4c2(y)
        y1x = self.f4b2(y1x, training=training)
        y3x = self.f4c3(y)
        y3x = self.f4b3(y3x, training=training)
        y = self.f4concat([y1x, y3x])

        # Fire 5
        y = self.f5c1(y)
        y = self.f5b1(y, training=training)
        y1x = self.f5c2(y)
        y1x = self.f5b2(y1x, training=training)
        y3x = self.f5c3(y)
        y3x = self.f5b3(y3x, training=training)
        y = self.f5concat([y1x, y3x])

        # Fire 6
        y = self.f6c1(y)
        y = self.f6b1(y, training=training)
        y1x = self.f6c2(y)
        y1x = self.f6b2(y1x, training=training)
        y3x = self.f6c3(y)
        y3x = self.f6b3(y3x, training=training)
        y = self.f6concat([y1x, y3x])

        # Fire 7
        y = self.f7c1(y)
        y = self.f7b1(y, training=training)
        y1x = self.f7c2(y)
        y1x = self.f7b2(y1x, training=training)
        y3x = self.f7c3(y)
        y3x = self.f7b3(y3x, training=training)
        y = self.f7concat([y1x, y3x])

        y = self.mp7(y)

        # Fire 8
        y = self.f8c1(y)
        y = self.f8b1(y, training=training)
        y1x = self.f8c2(y)
        y1x = self.f8b2(y1x, training=training)
        y3x = self.f8c3(y)
        y3x = self.f8b3(y3x, training=training)
        y = self.f8concat([y1x, y3x])

        y = self.avgpool(y)
        y = self.classifier(y)

        return y
