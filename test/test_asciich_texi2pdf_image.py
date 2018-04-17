import pytest

@pytest.fixture(scope='module')
def container_name():
    return 'asciich/texi2pdf'

@pytest.fixture(scope='module')
def contianer_volumes():
    return '$(pwd)/test:/test_data'

class TestAsciichTexi2pdfImage(object):

    def test_copy_testdata(self, docker_container):
        assert docker_container.file('/test_data').is_directory()

    def test_sample_a4_german(self):
        pass