#!/usr/bin/env python

import os
import subprocess

def bwa_align(genome_file, fastq, outfile):

    """
    Uses BWA MEM to align input fastq to a genome.

    :param genome_file: Genome file to be aligned to.
    :param fastq: Input fastq.
    :param outfile: Outfile (BAM format)
    """

    cmd = f'bwa mem {genome_file} {fastq} > {outfile}'
    os.system(cmd)

def convert_sam_bam(infile, bam_outfile):

    """
    Converts from SAM file format to BAM.

    :param infile: SAM file to be converted.
    :param bam_outfile: Outfile (BAM format)
    """

    cmd = f'samtools view -b {infile} -o {bam_outfile}'
    os.system(cmd)

def sort_bam(infile, sorted_outfile):

    """
    Sorts a BAM file.

    :param infile: Infile (BAM format)
    :param sorted_outfile: Sorted output (BAM format)
    """

    cmd = f'samtools sort -o {infile} {sorted_outfile}'
    os.system(cmd)

def index_bam(sorted_infile):

    """
    Indexes a BAM file.
    :param sorted_infile: Sorted BAM file.
    """

    cmd = f'samtools index {sorted_infile}'
    os.system(cmd)

def report_reads(sorted_infile):

    """
    Counts out total number of reads mapped in a BAM file.
    Requires index.

    :param sorted_infile: Sorted BAM file.
    :return: Number of mapped reads (str).
    """

    cmd = f'samtools view -c {sorted_infile}'

    result = subprocess.check_output(cmd, shell=True)
    return result.decode("utf-8")