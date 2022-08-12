from BCBio import GFF
import pandas as pd


def read_txt_list(file):
    return pd.read_table(file, header=None).iloc[:, 0].values

def gff_parse(gff_file, gff_type, id_list):

    position = list()

    ids = read_txt_list(id_list)

    in_handle = open(gff_file)
    # parse gff for each gff_id (chromosome, contig, scaffold) 
    for rec in GFF.parse(in_handle, limit_info=dict(gff_type=[gff_type])):
        # extract feature record for each gene or mRNA
        for feature in rec.features:
            name = feature.qualifiers["Name"][0]
            # only ids in input ID list
            if name in ids:
                position.append([
                    name,
                    rec.id,
                    int(feature.location.start),
                    int(feature.location.end)
                ])
    in_handle.close()

    position = pd.DataFrame(position, columns=["id", "chr", "start", "end"])
    position = position.sort_values(by=["chr", "start"])

    # check ids not in gff files
    order = [i for i in ids if i in position.id.values]
    noinfo = [i for i in ids if i not in position.id.values]
    if len(noinfo) > 0:
        print(noinfo, "are no information in gff file, so they are removed for further process.")

    return position, order


def csv_parse(gff_csv):
    position = pd.read_csv(gff_csv)
    order = position.id.values
    return position