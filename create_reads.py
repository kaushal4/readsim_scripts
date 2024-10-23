import argparse
import shlex
import subprocess


# Class to parse arguments
class Arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Generate reads from a reference genome')
        self.parser.add_argument('Sample 0', type=str, help='sample 0 fna file')
        self.parser.add_argument('Sample 1', type=str, help='sample 1 fna file')
        self.parser.add_argument('output_dir', type=str, help='Output Directory')
        self.sample_0 = None
        self.sample_1 = None
        self.output_dir = None
        self.parse_args()
    
    def parse_args(self):
        args = self.parser.parse_args()
        self.sample_0 = args.sample_0
        self.sample_1 = args.sample_1
        self.output_dir = args.output_dir
    
    def get_sample_0(self):
        return self.sample_0

    def get_sample_0(self):
        return self.sample_0

# ./dwgsim -1 100 -2 100 -y 0 ./inputs/sample2.fasta outputs/output1
class DwgsimRunner:
    def __init__(self, sample_0, output_dir):
        self.sample_0 = sample_0
        self.output_dir = output_dir

    def generate_reads(self):
        command = f"./dwgsim -1 100 -2 100 -y 0 -C 100 {self.sample_0} ${self.output_dir}/sample_0"
        args = shlex.split(command)

        result = subprocess.run(args, check=True)

def main():
    args = Arguments()
    args.parse_args()
    dwgsim_runner_sample_0 = DwgsimRunner(args.get_sample_0(), args.output_dir)
    dwgsim_runner_sample_1 = DwgsimRunner(args.get_sample_1(), args.output_dir)
    dwgsim_runner_sample_0.generate_reads()
    dwgsim_runner_sample_1.generate_reads()

if __name__ == "__main__":
    main()