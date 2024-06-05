import click
from bin import Fasta_ORF_Analysis, Fasta_Statistics, script3

@click.group()
def cli():
    """My Toolkit Command Line Interface"""
    pass

@cli.command()
@click.option('-f', '--fasta', required=True, help='Input FASTA file')
@click.option('-r', '--reading_frame', type=int, default=1, help='Reading frame (1, 2, or 3)')
@click.option('-n', '--repeat_length', type=int, required=True, help='Repeat length for substring analysis')
def Run_Fasta_ORF_Analysis(fasta, reading_frame, repeat_length):
    """Run script1"""
    import sys
    import subprocess

    # Construct command arguments
    cmd = ['python', '-m', 'my_toolkit.script1', '--fasta', fasta, '--reading_frame', str(reading_frame), '--repeat_length', str(repeat_length)]

    # Execute the script
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

@cli.command()
def Run_Fasta_Statistics(fasta, reading_frame, repeat_length):
    """Run script2"""
    import sys
    import subprocess

    # Construct command arguments
    cmd = ['python', '-m', 'Fasta_Stats', '--fasta', fasta]

    # Execute the script
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

@cli.command()
def run_accession_simplify(fasta_file, output_directory):
    """Run script3"""
    import sys
    import subprocess

    # Construct command arguments
    cmd = ['python', '-m', 'Simplify_Accession IDs', '--fasta', fasta_file, '--dir', output_directory]

    # Execute the script
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

if __name__ == "__main__":
    cli()