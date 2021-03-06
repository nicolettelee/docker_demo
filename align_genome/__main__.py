#!/usr/bin/env python

import argparse
import os
from align_genome.scripts import alignment_functions, cleanup_functions

def main(args):

    real_path = os.path.dirname(os.path.realpath(__file__))

    # set up

    tmp_dir = f'{real_path}/tmp'

    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)

    genome_file = f'{real_path}/resources/genome/genome.fa'
    #fastq_a = f'{real_path}/resources/fastqs/samples/A.fastq'
    fastq_a = args.fastq
    output_a = f'{tmp_dir}/aln_A.sam'
    output_a_bam = f'{tmp_dir}/aln_A.bam'
    sorted_a_bam = f'{tmp_dir}/aln_A.sorted.bam'

    # align
    print("Now performing alignment...")
    alignment_functions.bwa_align(genome_file, fastq_a, output_a)
    print("Alignment finished.")

    # convert
    print("Converting sam to bam...")
    alignment_functions.convert_sam_bam(output_a, output_a_bam)
    print("Conversion finished.")

    # sort
    print("Sorting bam file...")
    alignment_functions.sort_bam(output_a_bam, sorted_a_bam)
    print("Sorting finished.")

    # index
    print("Indexing bam...")
    alignment_functions.index_bam(sorted_a_bam)
    print("Indexing finished.")

    # report
    result = alignment_functions.report_reads(sorted_a_bam)
    print(f'Number of reads mapped to genome: {result}')

    # cleanup, finish

    if args.keep_bam:
        keep_flag = True
    else:
        keep_flag = False

    cleanup_functions.clear_dir(tmp_dir, keep_flag, sorted_a_bam)
    print("Pipeline finished!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Align fastqs to ref genome.")
    parser.add_argument("--fastq", type=str, required=True,
                        help="Path to fastq file.")
    parser.add_argument("--keep_bam", action="store_true", required=False,
                        help="Keep final bam file.")
    args = parser.parse_args()
    main(args)