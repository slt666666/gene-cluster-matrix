import argparse

# Following function parse input options.
def parse_args():
    parser = argparse.ArgumentParser(description='Generate distance matrix of gene cluster')
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('-g', '--gff', help='gff3 format file')
    group1.add_argument('-c', '--gff_csv', help='position data of csv file')
    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-i', '--id_list', help='Gene/mRNA id list')
    group2.add_argument('-t', '--tree', help='phylogenetic tree file')
    parser.add_argument('-o', '--out', required=True, help='Output file name prefix')
    parser.add_argument('-d', '--threshold', default=50000, help='Threshold of gene cluster distance', type=int)
    parser.add_argument('-f', '--gff_feature', default='gene', help='gff type (gene or mRNA)')
    parser.add_argument('-s', '--clade', help='clade information')
    args = parser.parse_args()
    return vars(args)