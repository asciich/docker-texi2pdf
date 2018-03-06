#!/usr/bin/env bash

set -e

docker run --rm -v $(pwd):/test_data -it asciich/texi2pdf /bin/bash -c "cp -rv /test_data /test_data_tmp && cd /test_data_tmp/ && texi2pdf sample.tex"

echo "Tests passed"