import sys

from parse_args import parse_args
from gff_parse import gff_parse, csv_parse
from make_plotly_data import calc_distance, heatmap_matrix, hover_text
from make_plotly_fig import heatmap

class GeneClusterMatrix:

    def __init__(self, gff, gff_type, id_list, threshold, out, tree, gff_csv, add):
        self.gff = gff
        self.gff_type = gff_type
        self.gff_csv = gff_csv
        self.id_list = id_list
        self.threshold = threshold
        self.add = add
        self.tree = tree
        self.out = out
    
    def main(self):

        position, order = gff_parse(self.gff, self.gff_type, self.id_list)

        # if self.gff_csv == None:
        #     position = gff_parse(self.gff_csv)
        # else:
        #     position = csv_parse(self.gff_file, self.gff_type, id_list)
        
        distance = calc_distance(position, order)

        z_data = heatmap_matrix(distance, self.threshold)
        text = hover_text(distance, order)

        # if self.add == None:
        #     zdata = heatmap_matrix(distance)
        #     text = hovertext(distance)
        # else:
        #     zdata = add_info(XXX)
        #     text = hovertext(position, distance, self.add)

        heatmap(z_data, text, order, self.out, self.tree)

def main() -> None:
    args_dict = parse_args()
    gcm = GeneClusterMatrix(**args_dict)
    gcm.main()

if __name__ == '__main__':
    main()