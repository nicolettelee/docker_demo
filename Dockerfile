FROM continuumio/miniconda3
COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "align", "/bin/bash", "-c"]

RUN echo "Making sure dependencies are installed:"
RUN bwa
RUN samtools