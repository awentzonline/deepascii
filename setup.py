#!/usr/bin/env python
from distutils.core import setup


setup(
    name='deepascii',
    version='0.0.1',
    description='Convert images to text art using deep neural networks',
    author='Adam Wentz',
    author_email='adam@adamwentz.com',
    url='https://github.com/awentzonline/deepascii',
    packages=[
        'deepascii',
    ],
    install_requires=[
        'Pillow',
        'numpy',
        'keras'
    ],
    scripts=[
        'scripts/make_deepascii.py'
    ]
)
