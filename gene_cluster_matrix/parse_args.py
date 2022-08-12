import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Generate distance matrix of gene cluster')
    parser.add_argument('gff', help='gff3 format file')
    parser.add_argument('gff_type', help='gff type (gene or mRNA)')
    parser.add_argument('id_list', help='Gene/mRNA id list')
    parser.add_argument('threshold', help='Threshold of gene cluster distance', type=int)
    parser.add_argument('out', help='Output file name prefix')
    parser.add_argument('--tree', '-t', help='phylogenetic tree file')
    parser.add_argument('--gff_csv', '-c', help='position data of csv file')
    parser.add_argument('--add', '-a', help='additional information to visualize in matrix')
    args = parser.parse_args()
    return vars(args)