import sys
import gffutils
import pandas as pd

from .make_tree import get_leaf_order


# Following functions generate position data from gff3 format file by "gffutils" library.
# gff_parse() function generate position data and id list ordered by id_list.
# gff_tree_parse() function generate position data and id list ordered by tree file.

def read_txt_list(file):
    return pd.read_csv(file, header=None).iloc[:, 0].values

def check_clade(order, clade):
    if clade != None:
        clade = read_txt_list(clade)
        if len([i for i in order if i not in clade]) > 0:
            print("Clade file missed some ids in id_list or tree or gff_csv file.")
            sys.exit()

def get_position_from_gff(gff_file, gff_feature, ids, out):
    print("start parse gff file.")
    position = list()
    
    db = gffutils.create_db(gff_file, ':memory:', merge_strategy='create_unique', keep_order=False, sort_attribute_values=False)
    for feature in db.features_of_type(gff_feature, order_by=['seqid', 'start']):
        name = feature.attributes['Name'][0]
        if name in ids:
            position.append([
                name,
                feature.seqid,
                int(feature.start),
                int(feature.end)
            ])

    position = pd.DataFrame(position, columns=["id", "chr", "start", "end"])
    position = position.sort_values(by=["chr", "start"])

    # check ids not in gff files
    order = [i for i in ids if i in position.id.values]
    noinfo = [i for i in ids if i not in position.id.values]
    if len(noinfo) > 0:
        print(noinfo, "are no information in gff file, so they are removed for further process.")
    if len(order) == 0:
        print("All provided ids could not get position data from gff file. -f option might be misspecified.")
        sys.exit()
    # save position data as csv file
    position.to_csv("{}_position.csv".format(out), index=None)
    print("finish generating {}_position.csv".format(out))
    return position, order

def gff_parse(gff_file, gff_feature, out, id_list, clade):
    ids = read_txt_list(id_list)
    position, order = get_position_from_gff(gff_file, gff_feature, ids, out)
    check_clade(order, clade)
    return position, order

def gff_tree_parse(gff_file, gff_feature, out, tree, clade):
    ids = get_leaf_order(tree)
    position, order = get_position_from_gff(gff_file, gff_feature, ids, out)
    check_clade(order, clade)
    return position, order

def csv_parse(gff_csv, clade, tree):
    position = pd.read_csv(gff_csv)
    order = position.id.values
    if tree != None:
        ids = get_leaf_order(tree)
        order = [i for i in ids if i in order]
    check_clade(order, clade)
    return position, order