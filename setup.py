# Author: Toshiyuki Sakai <toshi6661024@gmail.com>
# Copyright (c) 2022- Toshiyuki Sakai
# License: MIT

from setuptools import setup
import gene_cluster_matrix

DESCRIPTION = 'Visualization library for gene cluster & distance'
NAME = 'gene_cluster_matrix'
AUTHOR = 'Toshiyuki Sakai'
AUTHOR_EMAIL = 'toshi6661024@gmail.com'
URL = 'https://github.com/slt666666/gene_cluster_matrix'
LICENSE = 'MIT'
VERSION = gene_cluster_matrix.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'numpy',
    'pandas',
    'plotly',
    'gffutils',
    'toytree',
    'toyplot @ git+ssh://git@github.com/sandialabs/toyplot.git@8679e064549182428fa41b6b0ad3d71fbe2f1f1f#egg=toyplot',
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

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=LICENSE,
    url=URL,
    version=VERSION,
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
    packages=PACKAGES,
    entry_points=ENTRY_POINTS,
)
