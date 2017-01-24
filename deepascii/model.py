import os
import string

import numpy as np
from keras import backend as K
from keras.layers import Activation, Convolution2D, Layer, MaxPooling2D
from keras.models import Model
from keras.preprocessing.image import img_to_array
from PIL import Image, ImageFont, ImageDraw

from . import vgg16


class Argmax(Layer):
    def __init__(self, axis=0, *args, **kwargs):
        self.axis = axis
        super(Argmax, self).__init__(*args, **kwargs)

    def call(self, x, mask=None):
        return K.argmax(x, axis=self.axis)

    def get_output_shape_for(self, input_shape):
        return (input_shape[0],)


def make_model(img_shape, charset_features, layer_name='block3_conv1'):
    if K.image_dim_ordering():
        num_chars, char_h, char_w, char_channels = charset_features.shape
        axis = -1
    else:
        num_chars, char_channels, char_h, char_w = charset_features.shape
        axis = 1
    vgg = vgg16.VGG16(input_shape=img_shape, include_top=False)
    layer = vgg.get_layer(layer_name)

    features_W = charset_features.transpose((1, 2, 3, 0)).astype(np.float32)

    x = Convolution2D(
        num_chars, char_h, char_w, border_mode='full',
        weights=[features_W, np.zeros(num_chars)])(layer.output)
    x = MaxPooling2D((2, 2))(x)
    #x = Argmax(axis)(x)
    #model.add(Activation('softmax'))
    model = Model([vgg.input], [x])
    return model


def generate_charset(charset, font_file, font_size):
    font = ImageFont.truetype(font_file, font_size)
    max_w, max_h = 0, 0
    for char in charset:
        w, h = font.getsize(char)
        max_w = max(w, max_w)
        max_h = max(h, max_h)
    max_shape = (max_w, max_h)
    char_imgs = []
    for char in charset:
        img = Image.new('L', max_shape)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), char, font=font, fill='white')
        char_imgs.append(img_to_array(img))
    return np.stack(char_imgs)


def extract_charset_features(charset, layer_name='block3_conv1'):
    axis = dict(tf=-1, th=1)[K.image_dim_ordering()]
    shape = list(charset.shape[1:])
    shape[axis] = 3
    vgg = vgg16.VGG16(input_shape=shape, include_top=False)
    layer = vgg.get_layer(layer_name)
    layer_model = Model([vgg.input], [layer.output])
    layer_model.compile('adam', 'categorical_crossentropy')
    rgb_charset = np.repeat(charset, 3, axis)
    return layer_model.predict(vgg16.preprocess_input(rgb_charset))
