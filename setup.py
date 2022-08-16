# Author: Toshiyuki Sakai <toshi6661024@gmail.com>
# Copyright (c) 2022- Toshiyuki Sakai
# License: BSD 3 clause

from setuptools import setup
import gene_cluster_matrix

DESCRIPTION = 'Visualization library for gene cluster & distance'
NAME = 'gene_cluster_matrix'
AUTHOR = 'Toshiyuki Sakai'
AUTHOR_EMAIL = 'toshi6661024@gmail.com'
URL = 'https://github.com/slt666666/gene_cluster_matrix'
VERSION = gene_cluster_matrix.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'numpy',
    'pandas',
    'plotly',
    'gffutils',
    'toytree',
    'toyplot',
    'Pillow'
]

PACKAGES = [
    'gene_cluster_matrix'
]

ENTRY_POINTS = {
        'console_scripts': [
            'gene_cluster_matrix=gene_cluster_matrix.core:main'
        ],
    }

PYTHON_REQUIRES = '>=3.6'

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    version=VERSION,
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
    entry_points=ENTRY_POINTS,
)
