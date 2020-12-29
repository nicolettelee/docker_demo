# Docker demo project
The purpose of this project will be to test out the running of bwa and samtools using docker.

## Usage

Run 'docker build . -t align_genome' at the top level of the directory to build the image.

Command for running container with local file:
```
docker run -v [local input fastq path]:/app/align_genome/input.fastq -t align_genome:latest --fastq /app/align_genome/input.fastq
```

## Overview
- align the fastqs to the genome with bwa
- use samtools to convert, sort, and index bam file
- use samtools to count the number of reads aligned, and print output to sterr

