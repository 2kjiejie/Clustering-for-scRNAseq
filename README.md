# Clustering-for-scRNAseq
Pipelines and comparison for clustering approach in single cell RNA seq data.

1. Set up pipelines for raw SRA data preprocessing
2. Performing clustering analysis

## 1. From cell ranger to count matrix
Follow the instructions from [cell_ranger_pipelines](cell_ranger_pipelines.md) <br>
To transform raw .SRA files to count matrix produced by cell ranger pipelines

## 2. Data preprocessing
After getting raw count matrix, use preprocessing.Rmd files to preprocess the data

## 3. Benchmarking the clustering approach
Use [methods/](https://github.com/waynewu6250/Clustering-for-scRNAseq/tree/master/methods) to get the final cluster results

## 4. Compare them in two jupyter notebooks
1) [sc10x-3c](methods/Comparison-sc10x-3c.ipynb)
2) [sc10x-5c](methods/Comparison-sc10x-5c.ipynb)

