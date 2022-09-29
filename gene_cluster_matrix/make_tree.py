import toytree
import toyplot
import toyplot.png
import numpy as np
import pandas as pd
from PIL import Image, ImageOps


# Following functions generate phylogenetic tree image by "toytree" library.
# The input file is newick format.
# maketree() function generate tree image(png file) and customized PIL objects for matrix.

def get_leaf_order(tree, ids):
    # load a toytree from a newick string
    f = open(tree, 'r')
    nwk = f.read()
    f.close()
    tree = toytree.tree(nwk, tree_format=0)
    # remove tips (no info in gff file) from tree
    tree_ids = tree.get_tip_labels()
    drop_ids = [i for i in tree_ids if i not in ids]
    tree = tree.drop_tips(drop_ids)
    return tree.get_tip_labels()

def make_tree_figure(tree, out, order, clade):
    # load a toytree from a newick string
    f = open(tree, 'r')
    nwk = f.read()
    f.close()
    tree = toytree.tree(nwk, tree_format=0)

    # remove tips (no info in gff file) from tree
    tree_ids = tree.get_tip_labels()
    if len(tree_ids) != len(order):
        drop_ids = [i for i in tree_ids if i not in order]
        tree = tree.drop_tips(drop_ids)

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

    if clade != None:
        # add clade information
        clade = pd.read_csv(clade, index_col=0)
        clade_set = list(clade.clade.unique())
        # plot clade color
        axes.scatterplot(
            np.arange(tree.ntips),
            np.repeat(-0.1, tree.ntips),
            marker='s',
            size=25*180/tree.ntips,
            color=[toytree.colors[clade_set.index(clade.loc[i, "clade"])] for i in tree.get_tip_labels()],
            opacity=0.5,
        )

    toyplot.png.render(canvas, "{}_tree.png".format(out))
    print("finish generating {}_tree.png".format(out))

    # load image by PIL
    img = Image.open('{}_tree.png'.format(out))
    # make top tree image
    top_image = img.crop(img.getbbox())
    # make left tree image
    rotate_image = img.rotate(90, expand=True)
    left_image = ImageOps.flip(rotate_image.crop(rotate_image.getbbox()))

    return top_image, left_image

