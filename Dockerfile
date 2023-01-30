FROM mambaorg/micromamba:1.2.0
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
COPY --chown=$MAMBA_USER:$MAMBA_USER src/analyzer/* ./src/analyzer/

CMD ["python", "main.py"]