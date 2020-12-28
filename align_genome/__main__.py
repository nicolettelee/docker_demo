#!/usr/bin/env python

import os
import subprocess
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

    print("Converting sam to bam...")

    output_a_bam = f'{tmp_dir}/aln_A.bam'
    cmd = f'samtools view -b {output_a} -o {output_a_bam}'

    os.system(cmd)
    print("Conversion finished.")

    # sort

    print("Sorting bam file...")

    sorted_a_bam = f'{tmp_dir}/aln_A.sorted.bam'
    cmd = f'samtools sort -o {sorted_a_bam} {output_a_bam}'

    os.system(cmd)

    print("Sorting finished.")

    # index

    print("Indexing bam...")
    cmd = f'samtools index {sorted_a_bam}'

    os.system(cmd)

    print("Indexing finished.")

    # report

    print("Number of reads mapped to genome: ")

    cmd = f'samtools view -c {sorted_a_bam}'

    result = subprocess.check_output(cmd, shell=True)
    print(result.decode("utf-8"))

    # cleanup, finish
    print("Pipeline finished!")

if __name__ == "__main__":
    main()