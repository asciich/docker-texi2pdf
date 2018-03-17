#!/usr/bin/env bash

set -e

TEX_PATH=${1}
MAIN_WD=$(pwd)

TEX_DIR=$(cd $(dirname ${TEX_PATH}) && pwd)
TEX_FILE=$(basename ${TEX_PATH})
cd ${MAIN_WD}

docker run --rm -u $(id -u):$(id -g) -v ${TEX_DIR}:/texdir -it asciich/texi2pdf /bin/bash -c "cd /texdir && texi2pdf ${TEX_FILE}"