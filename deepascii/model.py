import os
import string

import numpy as np
from keras import backend as K
from keras.layers import Activation, AveragePooling2D, BatchNormalization, Convolution2D, Layer, MaxPooling2D
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


def make_model(
        img_shape, charset_features, layer_name='block2_conv1',
        output_pool=2, pool_type='max'):
    if K.image_dim_ordering():
        num_chars, char_h, char_w, char_channels = charset_features.shape
        axis = -1
    else:
        num_chars, char_channels, char_h, char_w = charset_features.shape
        axis = 1
    vgg = vgg16.VGG16(input_shape=img_shape, include_top=False)
    layer = vgg.get_layer(layer_name)
    x = layer.output
    # TODO: theano dim order
    features_W = charset_features.transpose((1, 2, 3, 0)).astype(np.float32)
    features_W = features_W[::-1, ::-1, :, :] / np.sqrt(np.sum(np.square(features_W), axis=(0, 1), keepdims=True))
    x = BatchNormalization(mode=2)(x)
    x = Convolution2D(
        num_chars, char_h, char_w, border_mode='valid',
        weights=[features_W, np.zeros(num_chars)])(x)
    if output_pool > 1:
        pool_class = dict(max=MaxPooling2D, avg=AveragePooling2D)[pool_type]
        x = pool_class((output_pool, output_pool))(x)
    #x = Argmax(axis)(x)
    model = Model([vgg.input], [x])
    return model


def generate_charset(charset, font_file, font_size, invert=False):
    fill_color, background_color = 'white', 'black'
    if invert:
        fill_color, background_color = background_color, fill_color
    font = ImageFont.truetype(font_file, font_size)
    max_w, max_h = 0, 0
    for char in charset:
        w, h = font.getsize(char)
        max_w = max(w, max_w)
        max_h = max(h, max_h)
    max_shape = (max_w, max_h)
    char_imgs = []
    for char in charset:
        img = Image.new('L', max_shape, background_color)
        draw = ImageDraw.Draw(img)
        draw.text((0,0), char, font=font, fill=fill_color)
        char_imgs.append(img_to_array(img))
    return np.stack(char_imgs)


def extract_charset_features(charset, layer_name='block2_conv1'):
    axis = dict(tf=-1, th=1)[K.image_dim_ordering()]
    shape = list(charset.shape[1:])
    shape[axis] = 3
    vgg = vgg16.VGG16(input_shape=shape, include_top=False)
    layer = vgg.get_layer(layer_name)
    layer_model = Model([vgg.input], [layer.output])
    layer_model.compile('adam', 'categorical_crossentropy')
    rgb_charset = np.repeat(charset, 3, axis)
    return layer_model.predict(vgg16.preprocess_input(rgb_charset))
