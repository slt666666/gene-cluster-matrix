import argparse

# Following function parse input options.
def parse_args():
    parser = argparse.ArgumentParser(description='Generate distance matrix of gene cluster')
    parser.add_argument('-g', '--gff', required=True, help='gff3 format file')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--id_list', help='Gene/mRNA id list')
    group.add_argument('-t', '--tree', help='phylogenetic tree file')
    group.add_argument('-c', '--gff_csv', help='position data of csv file')
    parser.add_argument('-o', '--out', required=True, help='Output file name prefix')
    parser.add_argument('-d', '--threshold', default=50000, help='Threshold of gene cluster distance', type=int)
    parser.add_argument('-f', '--gff_feature', default='gene', help='gff type (gene or mRNA)')
    parser.add_argument('-s', '--clade', help='clade information')
    args = parser.parse_args()
    return vars(args)