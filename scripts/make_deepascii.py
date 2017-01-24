#/usr/bin/env python
import argparse
import os

from deepascii.main import main


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Deep ASCII')
    argparser.add_argument('source_glob')
    argparser.add_argument('--font', default='DroidSansMono.ttf')
    argparser.add_argument('--font-size', type=int, default=12)
    config = argparser.parse_args()
    main(config)
