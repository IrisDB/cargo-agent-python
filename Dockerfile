# aka 1.2.0-jammy
FROM mambaorg/micromamba@sha256:5254e13db25eef59b6e2248ec02e8adfb82fd48cc23c6f92df648d8f0bc94cd8
LABEL org.opencontainers.image.authors="us@couchbits.com"
LABEL org.opencontainers.image.vendor="couchbits GmbH"

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

# the app
ENV PROJECT_DIR $HOME/cargo-agent-r
WORKDIR $PROJECT_DIR
COPY --chown=$MAMBA_USER:$MAMBA_USER main.py .
COPY --chown=$MAMBA_USER:$MAMBA_USER src/* ./src/

CMD ["python", "main.py"]