from gene_cluster_matrix import core

def test_matrix1():
    # basic matrix
    test1 = core.GeneClusterMatrix(
        gff="sample_data/sample.gff3",
        gff_csv=None,
        id_list="sample_data/id_list.txt",
        tree=None,
        out="test1",
        threshold=50000,
        gff_feature="mRNA",
        clade="sample_data/clade.csv"
        )
    test1.generate_matrix()

def test_matrix2():
    # matrix with tree
    test2 = core.GeneClusterMatrix(
        gff="sample_data/sample.gff3",
        gff_csv=None,
        id_list=None,
        tree="sample_data/sample.nwk",
        out="test2",
        threshold=50000,
        gff_feature="mRNA",
        clade=None
        )
    test2.generate_matrix()

def test_matrix3():
    # matrix with clade
    test3 = core.GeneClusterMatrix(
        gff="sample_data/sample.gff3",
        gff_csv=None,
        id_list="sample_data/id_list.txt",
        tree=None,
        out="test3",
        threshold=50000,
        gff_feature="mRNA",
        clade="sample_data/clade.csv"
        )
    test3.generate_matrix()

def test_matrix4():
    # matrix with tree and clade
    test4 = core.GeneClusterMatrix(
        gff="sample_data/sample.gff3",
        gff_csv=None,
        id_list=None,
        tree="sample_data/sample.nwk",
        out="test4",
        threshold=50000,
        gff_feature="mRNA",
        clade="sample_data/clade.csv"
        )
    test4.generate_matrix()

def test_matrix5():
    # matrix with tree and clade by position csv data
    test5 = core.GeneClusterMatrix(
        gff=None,
        gff_csv="sample_data/position.csv",
        id_list=None,
        tree="sample_data/sample.nwk",
        out="test5",
        threshold=50000,
        gff_feature="mRNA",
        clade="sample_data/clade.csv"
        )
    test5.generate_matrix()
