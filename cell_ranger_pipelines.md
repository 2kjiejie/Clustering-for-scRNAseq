# Cell Ranger Pipelines

Source: https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger

This is the manual for processing raw fastq files into count matrix file.

## 1. Cell ranger installation
Go to https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest and download the lastest verstion of cell ranger and references.

A. To unpack the cell ranger and script into a new directory called cellranger-3.1.0.
>
    tar -xzvf cellranger-3.1.0.tar.gz

B. Download and unpack any of the reference data files in a convenient location:
>  
    tar -xzvf refdata-cellranger-GRCh38-3.0.0.tar.gz

## 2. From .sra files to fastq
Go to NCBL website to download SRA toolkits
Download the SRA toolkits and install <br>
https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software 

Here we use sc_10x [(GSM3022245)](https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR6782112) for example, it uses GRCh38 for reference and expect-cells=4000. (It will specify in online SRA documentations.)
>
    wget https://sra-download.ncbi.nlm.nih.gov/traces/sra60/SRR/006623/SRR6782112

Then, locate to the sra-toolkit 
>
    ./bin/fastq-dump *.sra

For pair-ends:
>
    ./bin/fastq-dump --split-files *.sra

Then refer to [Cell-ranger pipelines](https://kb.10xgenomics.com/hc/en-us/articles/115003802691-How-do-I-prepare-Sequence-Read-Archive-SRA-data-from-NCBI-for-Cell-Ranger-):

Change the file name into: <br>
`[Sample Name]` _S1_L00 `[Lane Number]` _ `[Read Type]`_001.fastq.gz

For example:

incompatible: SRR6334436_1.fastq <br>
compatible: SRR6334436_S1_L001_R1_001.fastq

## 3. From fastq files to cell count
Specify all the folders and run the following commands:
>
    cellranger count --id=sample1 \
                   --transcriptome=refdata-cellranger-GRCh38-3.0.0 \
                   --fastqs=fastq_path \
                   --sample=SRR6334436 \
                   --expect-cells=4000

##For example, here mysample could be SRR6334436##


## 4. Collect the information
It will mainly store all the information in the outs/ folder and the required folder will tree as follows:
 ```
 outs/
└── raw_feature_bc_matrix/
    ├── matrix.mtx.gz                                 
    ├── features.tsv.gz                           
    ├── barcodes.tsv.gz
└── filtered_feature_bc_matrix/
    ├── matrix.mtx.gz                                 
    ├── features.tsv.gz                           
    ├── barcodes.tsv.gz 
├── web_summary.html
```

1. **matrix.mtx.gz**: <br>
format is described as follows: <br>
For example, if a line in mtx file is 154 1 21, this indicates:
```
The gene at line number 154 in genes.tsv.

The cell-barcode at line number 1 in barcodes.tsv.

UMI count = 21 for the gene and barcode combination.
```
2. **genes.tsv**: <br>
This file contains all annotated genes. Each gene is represented in each row. The first column is the gene_id while the second column is the gene name.

3. **barcodes.tsv**: <br>
This file contains the barcodes represented in the mtx file. The folder filtered_gene_bc_matrices contains all barcodes that were filtered as cells. The folder raw_gene_bc_matrices contains all valid barcodes (that is all barcodes that came from a barcode whitelist).

\<Transform to CSV>\
These data are stored in sparse way. But you could also use the following command to transform the data into csv files:
>
    cellranger mat2csv sample123/outs/filtered_feature_bc_matrix sample123.csv


# CellRanger Four pipelines: 
1. cellranger mkfastq: <br>
Turn BCL files (raw base call files) into FASTQ files

2. cellranger count: <br>
Take FASTQ files and perform alignment.

3. cellranger aggr: <br>
Aggregate outputs from multiple runs of cellranger count. Combine data from multiple samples.

4. cellranger reanalyze: <br>
Rerun dimensionality reduction, clustering and gene expression algorithms of feature-barcode matrices.


