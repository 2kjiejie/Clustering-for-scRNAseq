# Clustering-for-scRNAseq
Pipelines and comparison for clustering approach in single cell RNA seq data.
There are totally 6 approaches and 7 protocols for comparison on a single cell RNA sequencing benchmark dataset [GSE118767](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE118767):

* Mixture of H2228, H1975 and HCC827 human lung cancer cell lines:
[SRR6782112](https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR6782112)
* Mixture of H2228, H1975, A549, H838 and HCC827 human lung cancer cell lines:
[SRR8606521](https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR8606521)

## Procedures

## 1. Upstream Analysis: 
From cell ranger to count matrix
>
    Raw SRA data -> fastq files -> count matrices

Follow the instructions from [cell_ranger_pipelines](cell_ranger_pipelines.md) <br> to transform raw .SRA files to count matrix produced by cell ranger pipelines.

## 2. Downstream Analysis: 
Performing clustering analysis on count matrices:

1. **Data preprocessing and Benchmarking**:
After getting raw count matrix, use the following files for data preprocessing and running the clustering algorithms:
<br> -> [3 cell lines](https://github.com/waynewu6250/Clustering-for-scRNAseq/blob/master/run_3c.Rmd)
<br> -> [5 cell lines](https://github.com/waynewu6250/Clustering-for-scRNAseq/blob/master/run_5c.Rmd)
<br> -> [subsampling](https://github.com/waynewu6250/Clustering-for-scRNAseq/blob/master/run_sub.Rmd)

    (Reference for individual methods could be looked up in [methods/](https://github.com/waynewu6250/Clustering-for-scRNAseq/tree/master/methods))

2. Compare them in two jupyter notebooks
<br> -> [sc10x-3c](Comparison-sc10x-3c.ipynb)
<br> -> [sc10x-5c](Comparison-sc10x-5c.ipynb)
<br> -> [sc10x-3c-subsampling](Comparison-sc10x-3c-sub.ipynb)
<br> -> [sc10x-5c-subsampling](Comparison-sc10x-5c-sub.ipynb)

