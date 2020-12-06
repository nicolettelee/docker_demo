#!/usr/bin/env python

import os
from align_genome.scripts import classes, config, say_hello

def main():

    real_path = os.path.dirname(os.path.realpath(__file__))

    # set up

    tmp_dir = f'{real_path}/tmp'

    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)

    genome_file = f'{real_path}/resources/genome/genome.fa'
    fastq_a = f'{real_path}/resources/fastqs/samples/A.fastq'
    output_a = f'{tmp_dir}/aln_A.sam'

    cmd = f'bwa mem {genome_file} {fastq_a} > {output_a}'

    # align

    print("Now performing alignment...")
    os.system(cmd)
    print("Alignment finished.")

    # convert

    # sort

    # index

    # report


if __name__ == "__main__":
    main()