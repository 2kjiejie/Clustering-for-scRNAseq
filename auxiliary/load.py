import csv
import gzip
import os
import scipy.io
import pandas as pd

class RNAdata:

    def __init__(self, matrix_dir):

        self.matrix_dir = matrix_dir
        self.mat = scipy.io.mmread(os.path.join(matrix_dir, "matrix.mtx.gz"))
        self.data = self.mat.toarray()
        self.percentage = len(self.data[self.data!=0])/(self.data.shape[0]*self.data.shape[1])
        self.features = self.make_features(self.matrix_dir)
        self.barcodes = self.make_barcodes(self.matrix_dir)

    def make_features(self, matrix_dir):

        features_path = os.path.join(matrix_dir, "features.tsv")
        df = pd.read_csv(features_path, delimiter="\t", names=["feature_id", "gene_name", "feature_type"])
        return df
    
    def make_barcodes(self, matrix_dir):

        barcodes_path = os.path.join(matrix_dir, "barcodes.tsv")
        barcodes = [row[0] for row in csv.reader(barcodes_path, delimiter="\t")]
        return barcodes

if __name__ == "__main__":
    data = RNAdata("dataset/sc-10x/filtered_feature_bc_matrix")
