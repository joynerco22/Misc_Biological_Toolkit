## Retrieve the accession  number and original sequence for a query multi-fasta file 
import sys
import argparse
import os

def accession_simplify(fasta_file, output_directory):
    os.makedirs(output_dir, exist_ok=True)

    # Construct the output file path
    base_name = os.path.basename(fasta_file)
    output_file = os.path.join(output_dir, base_name + '.txt')


    with open(fasta_file, 'r') as fp1, open(fasta_file + '.txt', 'w') as fp2:
        lines = fp1.readlines()

        for line in lines:
            if len(line) > 1 and line[0] == '>':
                segs = line.split('[')
                if len(segs) > 1:
                    nameList = segs[1].split(' ')
                    genus = segs[0]
                    if len(nameList[1]) >= 6:
                        species = nameList[1][0:5]
                    else:
                        species = nameList[1]
                    organism = genus + "_" + species
                    if organism[-1] != '\n':
                        organism = organism + '\n'
                else:
                    organism = ''
                    segs = segs[0].split(' ')
                    gi = segs[0]
                fp2.write('>' + gi + '\n')
            else:
                if len(line) > 1 and line[-2] != ']':
                    fp2.write(line)

def main():
    parser = argparse.ArgumentParser(description='Simplify the accession for a multi-fasta file')
    
    # Positional argument
    parser.add_argument('-i', '--fasta', required=True, help='Input FASTA file')

    args = parser.parse_args()
    
    accession_simplify(args.fasta_file)

if __name__ == "__main__":
    main()