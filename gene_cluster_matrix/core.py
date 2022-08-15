import sys

from .parse_args import parse_args
from .gff_parse import gff_parse, gff_tree_parse, csv_parse
from .make_plotly_data import calc_distance, heatmap_matrix, hover_text
from .make_plotly_fig import heatmap, heatmap_with_tree
from .make_tree import get_leaf_order


class GeneClusterMatrix:
    """gene cluster matrix visualizes gene pairs that are located in close position.
    X-axis and Y-axis of matrix are interest gene lists.
    Matrix is colored by the distance between 2 gene in X-axis and Y-axis.
    And only gene pair that distance is less than threshold (like ~50kbp) is colored.

    Input
    ----------
    gff         (-g): gff3 format file name, Annotation information of reference genome
    id_list     (-i): txt file name, Ordered Gene/mRNA id list
    tree        (-t): newick format file name, Phylogenetic tree file (newick format)
    gff_csv     (-c): csv format file name, Position data of csv file
    (id_list or tree or gff_csv is required to specify gene order)
    out         (-o): string , Output file name prefix
    threshold   (-d): int default:5000, Threshold distance to define gene cluster
    gff_feature (-f): string (gene or mRNA), Specify gff type (gene or mRNA) depending on the input ids
    clade       (-s): csv format file name, Clade information to separate gene/mRNA ids

    Examples
    --------
    # simple matrix
    gene_cluster_matrix -g sample.gff3 -i id_list.txt -o test
    # matrix with phylogenetic tree & clade information
    gene_cluster_matrix -g sample.gff3 -t tree.nwk -o test -s clade.csv
    """
    def __init__(self, gff, gff_feature, id_list, threshold, out, tree, gff_csv, clade):
        self.gff = gff
        self.gff_feature = gff_feature
        self.id_list = id_list
        self.threshold = threshold
        self.out = out
        self.tree = tree
        self.gff_csv = gff_csv
        self.clade = clade
    
    def get_position_and_order(self):
        # return position/ordered ids from gff file or csv file or tree file
        if self.id_list != None:
            return gff_parse(self.gff, self.gff_feature, self.out, self.id_list)
        elif self.gff_csv != None:
            return csv_parse(self.gff_csv, self.clade)
        elif self.tree != None:
            return gff_tree_parse(self.gff, self.gff_feature, self.out, self.tree)

    def generate_matrix(self):
        # extract gene positions from gff file
        position, order = self.get_position_and_order()
        # calculate distance between genes
        distance = calc_distance(position, order)
        # generate input data for plotly
        z_data = heatmap_matrix(distance, self.threshold)
        text = hover_text(distance, order, self.clade)
        # generate html file by plotly
        if self.tree == None:
            # make heatmap
            heatmap(z_data, text, order, self.out, self.clade)
        else:
            # make heatmap with phylogenetic tree
            heatmap_with_tree(z_data, text, order, self.out, self.tree, self.clade)

def main() -> None:
    args_dict = parse_args()
    gcm = GeneClusterMatrix(**args_dict)
    gcm.generate_matrix()

if __name__ == '__main__':
    main()