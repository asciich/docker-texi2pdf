# asciich/texi2pdf container

This container can be used to convert a *.tex file into a PDF.
Simply replace YOUR_TEX_FILE.tex at the end of this command before starting the container:

```
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/texdir -it asciich/texi2pdf /bin/bash -c "cd /texdir && texi2pdf YOUR_TEX_FILE.tex"
```

## Docker hub

This container is available on DockerHub: https://hub.docker.com/r/asciich/texi2pdf/

## Test container

Run tox to test the container:

```
tox
```