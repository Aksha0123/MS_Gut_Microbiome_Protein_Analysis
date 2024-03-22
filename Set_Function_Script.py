import csv
def read_proteins_from_tsv(file_path):
    """
    Reads protein names from a TSV file and returns a set of unique protein names.
    Assumes that protein names are in the first column of the TSV file.
    """
    proteins = set()
    with open(file_path, 'r') as file:
        for line in file:
            protein = line.strip().split('\t')[-1]
            proteins.add(protein)
    return proteins

def find_common_proteins(file1_path, file2_path):
    """
    Finds common proteins between two TSV files.
    """
    proteins_file1 = read_proteins_from_tsv(file1_path)
    proteins_file2 = read_proteins_from_tsv(file2_path)
    common_proteins = proteins_file1.intersection(proteins_file2)
    return common_proteins

def Convert_Csv(result, output_file):
    with open(output_file, 'w') as result_file:
        for r in result:
            result_file.write(r + "\n")

def find_different_proteins(proteins_file1, proteins_file2):
    different_proteins = proteins_file1 - proteins_file2
    return different_proteins

if __name__ == "__main__":
    # MS
    file1_path = "PROKKA_ERR2784696.tsv"  # Path to the first TSV file
    file2_path = "PROKKA_ERR2784700.tsv"  # Path to the second TSV file
    file3_path = "PROKKA_ERR2784708.tsv"
    file4_path = "PROKKA_ERR2784716.tsv"

    # Control
    file5_path = "PROKKA_ERR2784728.tsv"
    file6_path = "PROKKA_ERR2784732.tsv"
    file7_path = "PROKKA_ERR2784739.tsv"
    file8_path = "PROKKA_ERR2784745.tsv"


    MS_common_proteins1 = find_common_proteins(file1_path, file2_path)
    MS_common_proteins2 = find_common_proteins(file3_path, file4_path)
    ms_common_proteins_fin = set(MS_common_proteins1).intersection(set(MS_common_proteins2))

    Control_common_proteins1 = find_common_proteins(file5_path, file6_path)
    Control_common_proteins2 = find_common_proteins(file7_path, file8_path)
    control_common_proteins_fin = set(Control_common_proteins1).intersection(set(Control_common_proteins2))

    ms_different_proteins = find_different_proteins(ms_common_proteins_fin, control_common_proteins_fin)
    control_different_proteins = find_different_proteins(control_common_proteins_fin, ms_different_proteins)

    #print("Common proteins:")
    #for protein in common_proteins_fin:
       # print(protein)

    Convert_Csv(ms_common_proteins_fin, "MS_AfricanAmerican_Common.csv")
    Convert_Csv(control_common_proteins_fin, "Control_AfricanAmerican_Common.csv")
    Convert_Csv(ms_different_proteins, "MS_AfricanAmerican_Different_Proteins.csv")
    Convert_Csv(control_different_proteins, "Control_AfricanAmerican_Different_Proteins.csv")