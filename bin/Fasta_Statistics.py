from Bio import SeqIO
import sys

def gc_percent(fasta_file):
    count_seqs = {'A': 0, "C": 0, "T": 0, "G": 0}
    total_length = 0
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        total_length += len(sequence)
        
        for nucleotide in sequence:
            if nucleotide in count_seqs:
                count_seqs[nucleotide] += 1
                
    gc_content = ((count_seqs["C"] + count_seqs["G"]) / total_length) * 100
    print(f"GC Percentage is: {gc_content:.2f}%")

def fasta_statistics(fasta_file):
    lengths = [len(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    total_length = sum(lengths)
    num_sequences = len(lengths)
    max_length = max(lengths)
    min_length = min(lengths)
    avg_length = total_length / num_sequences if num_sequences > 0 else 0

    print(f"Number of sequences: {num_sequences}")
    print(f"Total length: {total_length}")
    print(f"Maximum length: {max_length}")
    print(f"Minimum length: {min_length}")
    print(f"Average length: {avg_length:.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_fasta_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    fasta_statistics(input_file)
    gc_percent(input_file)