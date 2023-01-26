#!/bin/bash --login
# kudos: https://towardsdatascience.com/conda-pip-and-docker-ftw-d64fe638dc45
set -e
conda activate "$ENV_PREFIX"
exec "$@"
