import string

import numpy as np
from keras import backend as K
from keras.preprocessing.image import img_to_array
from PIL import Image

from . import vgg16
from .model import extract_charset_features, generate_charset, make_model


def main(config):
    source_img = Image.open(config.source_glob)
    source_img = source_img = source_img.convert('L').convert('RGB')
    feature_axis = dict(tf=-1, th=1)[K.image_dim_ordering()]
    source_arr = img_to_array(source_img)
    print('Input image {} shape {}'.format(config.source_glob, source_arr.shape))

    print('Generating charset images...')
    if config.charset:
        charset_chars = config.charset
    else:
        charset_chars = string.letters + string.digits + """\/|-@.;:#+$_`~ """
    charset_imgs = generate_charset(
        charset_chars, config.font, config.font_size, invert=config.invert_color)
    print('Charset = ' + charset_chars)
    print('Extracting features from charset...')
    features = extract_charset_features(charset_imgs, layer_name=config.layer)
    print('Creating network...')
    model = make_model(
        source_arr.shape, features, layer_name=config.layer,
        output_pool=config.pool, pool_type=config.pool_type)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    print('Predicting...')
    z = model.predict(vgg16.preprocess_input(source_arr[None, ...]))
    indexes = np.argmax(z, axis=feature_axis).squeeze()
    for row in range(0, indexes.shape[0], 2):
        line = ''
        for col in range(0, indexes.shape[1], 1):
            line += charset_chars[indexes[row, col]]
        print line
