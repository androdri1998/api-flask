# -*- coding: utf-8 -*-


# Third
from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api flask'
__long_description__ = 'Uma api python com flask'

__author__ = 'André Rodrigues'
__author_email__ = 'andre@mail.com'

setup(
    name = 'api',
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    packages = find_packages(),
    license = 'MIT',
    description = __description__,
    long_description = __long_description__,
    url = '',
    keywords = 'API',
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
)