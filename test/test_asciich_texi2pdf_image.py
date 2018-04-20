import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/texi2pdf'

@pytest.fixture(scope='module')
def contianer_volumes():
    return '$(pwd)/test:/test_data'

class TestAsciichTexi2pdfImage(object):

    def test_container_image(self,  docker_container):
        assert docker_container.image.name == 'asciich/texi2pdf'

    def test_tex2pdf_available(self, docker_container):
        assert docker_container.exists('texi2pdf')