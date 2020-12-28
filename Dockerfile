FROM continuumio/miniconda3
WORKDIR /app
COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "align", "/bin/bash", "-c"]

COPY align_genome/ align_genome/
ENTRYPOINT ["conda", "run", "-n", "align", "python", "-m", "align_genome"]