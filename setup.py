# -*- coding: utf-8 -*-

import setuptools

metadata = {}
exec(compile(open("amazon/metadata.py").read(), "amazon/metadata.py", 'exec'), metadata)

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-amazon-unthrottled-paapi',
    version=metadata['__version__'],
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    description='Amazon Unthrottled Access to Amazon Product Advertising API for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=metadata['__license__'],
    url='https://github.com/nhapentor/python-amazon-unthrottled-paapi',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='amazon, product advertising, paapi, api'
)