# aka 1.2.0-bullseye-slim
FROM mambaorg/micromamba@sha256:1d05a8a7d88142f8225927756272748bc5feb438c0185de362e98ae5d88bf2f4
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