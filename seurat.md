# Seurat Notes
>
    pbmc.data <- Read10X(data.dir = "./dataset/pbmc3k/filtered_gene_bc_matrices/hg19/")
This command will read data from 10X output

>
    pbmc.data
    pbmc@meta.data
    pbmc[["RNA"]]@data
    pbmc[["RNA"]]@scale.data
This will store the data of pbmc with row as gene features and column as cell barcode and use indexing i.e. pbmc[c("a", "b"), 1:30] to subscript data. <br>
The second one will store metadata (quality control matrix) which gives some reference for each cell (barcode).

>
    pbmc[["percent.mt"]] <- PercentageFeatureSet(pbmc, pattern = "^MT-")
[[ ]] can be used to add columns in meta data

>
    pbmc <- subset(pbmc, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 5)
Use subset function to filter out the data