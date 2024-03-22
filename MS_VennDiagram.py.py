import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import pandas as pd

def read_tsv(file_path):
    data = pd.read_csv(file_path, sep='\t')
    return set(data['Value'])

def create_venn_diagram(data1, data2, data3, labels=('African American', 'Hispanic', 'White')):
    plt.figure(figsize=(8, 6))
    venn = venn3(subsets=(len(data1 - data2 - data3),
                          len(data2 - data1 - data3),
                          len(data1 & data2 - data3),
                          len(data3 - data1 - data2),
                          len(data1 & data3 - data2),
                          len(data2 & data3 - data1),
                          len(data1 & data2 & data3)),
                 set_labels=labels)

    plt.title("Proteins Identified of MS")
    plt.show()

if __name__ == "__main__":
    # Example data file paths, replace them with your own TSV files
    file1 = "data1.tsv"
    file2 = "data2.tsv"
    file3 = "data3.tsv"

    # Read data from TSV files into sets
    set1 = read_tsv(file1)
    set2 = read_tsv(file2)
    set3 = read_tsv(file3)

    # Create Venn diagram
    create_venn_diagram(set1, set2, set3)