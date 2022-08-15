import toytree
import toyplot
import toyplot.png
import numpy as np
from PIL import Image, ImageOps


# Following functions generate phylogenetic tree image by "toytree" library.
# The input file is newick format.
# maketree() function generate tree image(png file) and customized PIL objects for matrix.

def get_leaf_order(tree):
    # load a toytree from a newick string
    f = open(tree, 'r')
    nwk = f.read()
    f.close()
    tree = toytree.tree(nwk, tree_format=0)
    return tree.get_tip_labels()

def make_tree_figure(tree, out):
    # load a toytree from a newick string
    f = open(tree, 'r')
    nwk = f.read()
    f.close()
    tree = toytree.tree(nwk, tree_format=0)

    # setting parameters of tree components
    params = {
        "layout": 'd',
        "edge_type": 'p',
        "edge_style": {
            "stroke": toytree.colors[2],
            "stroke-width": 15,
        },
        "tip_labels_align": True,
        "tip_labels": False,
        "node_labels": False,
    }
    # generate png file
    canvas, axes, mark = tree.draw(height=1000, width=4000, **params)
    toyplot.png.render(canvas, "{}_tree.png".format(out))

    # load image by PIL
    img = Image.open('{}_tree.png'.format(out))
    # make top tree image
    img = ImageOps.mirror(img)
    top_image = img.crop(img.getbbox())
    # make left tree image
    rotate_image = img.rotate(90, expand=True)
    left_image = ImageOps.flip(rotate_image.crop(rotate_image.getbbox()))

    return top_image, left_image

