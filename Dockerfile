FROM continuumio/miniconda3
COPY environment.yml .
COPY align_genome/ align_genome/
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "align", "/bin/bash", "-c"]

RUN python -m align_genome
RUN echo "Finished"