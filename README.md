# Gene Cluster Matrix

<p><img src="https://github.com/slt666666/gene_cluster_matrix/blob/main/image/sample_matrix.png?raw=true"　itemprop="image" width="350" align="right" />
<a href="https://zenodo.org/badge/latestdoi/524101848"><img src="https://zenodo.org/badge/524101848.svg" alt="DOI"></a>
<h2>Description</h2>
<strong>Gene cluster matrix</strong> is a command line tool to generate matrix that visualize distances between genes that construct gene clusters. The matrix is generated as interactive html file. This tool can also visualize phylogenetic tree, so it can be useful to classify gene clusters into phylogenetically related clusters & phylogenetically unrelated gene clusters.</p>

Gene cluster matrix is developed by Python program and distributed under the MIT license.

## Install

1. install toyplot

`pip install --requirement https://raw.githubusercontent.com/slt666666/gene-cluster-matrix/main/requirements.txt`

2. install other libraries

`pip install gene_cluster_matrix`

## Dependencies
gene_cluster_matrix requires below libraries. (`pip install` automatically install dependencies)
* python (>= 3.6)
* numpy (>= 1.20.0)
* pandas (>= 1.2.0)
* plotly (>= 5.3.0)
* gffutils (>= 0.11.0)
* toytree (>= 2.0.1)
* Pillow (>= 9.2.0)

`toyplot` library is required to install independently.
* toyplot (>= 1.0.2.dev0)

`ghostscript` is required to generate phylogenetic tree image.

c.f.) Linux:`sudo apt-get install ghostscript`, Mac:`brew install ghostscript`

Windows: https://ghostscript.com/releases/gsdnld.html

## Usage example1: Distance matrix

<p><img src="https://github.com/slt666666/gene_cluster_matrix/blob/main/image/usage1.png?raw=true"　itemprop="image" width="200" align="right" />
The distance matrix visualize gene clusters. Gene cluster is a group of two or more genes that located within a few thousand ~ tens thousand base pairs of each other. The matrix also visualize distances between genes in the gene cluster as a color. In here, distance means physical distance in nucleotides in the genome.</p>

* simple distance matrix (the order is the given list order)

`gene_cluster_matrix -g sample.gff3 -i id_list.txt -f mRNA -o output_name`

* simple distance matrix. Set distance threshold as 100000bp to define gene cluster.

`gene_cluster_matrix -g sample.gff3 -i id_list.txt -d 100000 -f mRNA -o output_name`

* simple distance matrix by hand-made position data (the order is the given list order)

`gene_cluster_matrix -p position.csv -i id_list.txt -f mRNA -o output_name`

## Usage example2: Distance matrix with phylogenetic tree (& clade information)

<p><img src="https://github.com/slt666666/gene_cluster_matrix/blob/main/image/usage2.png?raw=true"　itemprop="image" width="250" align="right" />
Basically, there are 2 cases; Case 1 is genes in cluster show a similar function. Case 2 is genes in cluster show different functions. To identify case 2 type, phylogenetic analysis is one of the useful approaches. By ordering genes in distance matrix based on phylogenetic tree, we can identify gene clusters that consist of phylogenetically related genes and gene clusters that consist of phylogenetically unrelated genes.

This library enable us to visualize distance matrix of Usage example1 ordered by provided phylogenetic tree file. And if phylogenetic clade information is also provided, it will be also visualized.</p>

* distance matrix with phylogenetic tree (the order is the given tree tips)

`gene_cluster_matrix -g sample.gff3 -t sample.nwk -f mRNA -o output_name`

* distance matrix with phylogenetic tree & clade information (the order is the given tree tips)

`gene_cluster_matrix -g sample.gff3 -t sample.nwk -c clade.csv -f mRNA -o output_name`

### Input & Option
```
(required)
-g or -p … GFF3 fomrat file of reference genome (gff3 file) / position data file (csv file, format should be same as sample_data/position.csv)
-i or -t … Gene id list ordered by your preference (txt file) / phylogenetic tree file (newick format)
-f … Specify gff feature type (gene or mRNA) of input ids (string. default=gene)
-o … Output file name (string)
(optional)
-d … Threshold distance (bp) to define gene cluster (int. default=50000)
-c … Clade information for each gene/mRNA id. (csv file. format should be same as sample_data/clade.csv)
```

### Output
```
XXX.html or XXX_with_tree.html … interactive html file that visualize gene cluster matrix
XXX_position.csv … position data for each id in input such as id_list or tree
XXX_tree.png … phylogenetic tree figure (if -t option is used)
```

### Example
To view the examples, clone the gene_cluster_matrix repository and run by sample data:

```
$ git clone https://github.com/slt666666/gene_cluster_matrix.git
$ cd gene_cluster_matrix/sample_data
$ gene_cluster_matrix -g sample.gff3 -t sample.nwk -c clade.csv -f mRNA -o test
```
After running above commands, html file is generated in sample_data directory.

## Licence

[MIT](https://github.com/slt666666/gene_cluster_matrix/blob/main/LICENSE)

## Author

[Toshiyuki Sakai](https://github.com/slt666666)