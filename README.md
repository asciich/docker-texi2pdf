# asciich/texi2pdf container

This container can be used to convert a *.tex file into a PDF.
Simply replace YOUR_TEX_FILE.tex at the end of this command before starting the container:

```
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/texdir -it asciich/texi2pdf /bin/bash -c "cd /texdir && texi2pdf YOUR_TEX_FILE.tex"
```

## Docker hub

This container is available on DockerHub: https://hub.docker.com/r/asciich/texi2pdf/

## Test container

Currently the only existing test is to generate a PDF file from my
[sample posted long time ago on my personal blog.](https://asciich.ch/wordpress/software/latex/a4-dokumentenvorlage-in-latex/)


