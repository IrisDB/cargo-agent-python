FROM condaforge/mambaforge

# kudos: https://towardsdatascience.com/conda-pip-and-docker-ftw-d64fe638dc45

# Security Aspects
# Create a non-root user
ARG username=moveapps
ARG uid=1001
ARG gid=staff
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER

RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --ingroup $GID \
    --home $HOME \
    $USER

USER $USER

# the app
ENV PROJECT_DIR $HOME/cargo-agent-r
WORKDIR $PROJECT_DIR

ENV ENV_PREFIX $PROJECT_DIR/python-env
COPY --chown=$UID:$GID environment.yml .
RUN mamba env create --prefix $ENV_PREFIX --file environment.yml

COPY --chown=$UID:$GID main.py .
COPY --chown=$UID:$GID cargo_agent_python ./
COPY --chown=$UID:$GID start-process.sh .

ENTRYPOINT ["./start-process.sh"]

CMD ["python", "main.py"]