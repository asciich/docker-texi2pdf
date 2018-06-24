# conftest.py for docker image testing

import docker
import pytest


class DockerContainerError(Exception):
    pass


class DockerContainerExecError(DockerContainerError):
    pass

class DockerContainerFile():

    def __init__(self, docker_container, path):
        self._docker_container = docker_container
        self._path = path

    @property
    def exists(self):
        if self.is_file:
            return True
        if self.is_directory:
            return True
        return False

    @property
    def is_directory(self):
        try:
            self._docker_container.check_output('test -d {}'.format(self._path))
            return True
        except DockerContainerExecError as e:
            return False

    @property
    def is_executable(self):
        try:
            self._docker_container.check_output('test  -x {}'.format(self._path))
            return True
        except DockerContainerExecError as e:
            return False

    @property
    def is_file(self):
        try:
            self._docker_container.check_output('test -f {}'.format(self._path))
            return True
        except DockerContainerExecError as e:
            return False

class DockerContainerImage():

    def __init__(self, container_image):
        self._container_image = container_image

    @property
    def name(self):
        image_name = self._container_image.tags[0]
        image_name = image_name.split(':')[0]
        return image_name

    @property
    def tag(self):
        tag_name = self._container_image.tags[0]
        tag_name = tag_name.split(':')[1]
        return tag_name

class DockerContainer():

    def __init__(self, container_image):
        self._image = container_image
        self._client = docker.from_env()
        self._container = None

    def check_output(self, command):
        ret =  self._container.exec_run(command)
        if ret.exit_code != 0:
            raise DockerContainerExecError(ret.output)
        return ret.output

    def exists(self, command):
        """
        Implement command exists like testinfra: http://testinfra.readthedocs.io/en/latest/modules.html#testinfra.modules.file.File
        :param command:
        :return:
        """
        if command.startswith('/'):
            command_file = self.file(command)
            if command_file.is_executable:
                return True
        else:
            for path in self.get_env('PATH').split(':'):
                command_path = '{}/{}'.format(path, command)
                command_file = self.file(command_path)
                if command_file.is_executable:
                    return True
        return False

    def file(self, path):
        return DockerContainerFile(self, path)

    @property
    def default_command(self):
        return '/bin/sh -c "sleep 10000"'

    def get_env(self, env_name):
        """
        Get environment variable content
        :param env_name:
        :return:
        """
        return self.check_output('/bin/sh -c "echo ${}"'.format(env_name)).decode().strip()

    @property
    def id(self):
        return self._container.id

    @property
    def name(self):
        return self._container.name

    @property
    def image(self):
        return DockerContainerImage(self._container.image)

    def kill(self):
        self._container.kill()

    def run(self):
        self._container = self._client.containers.run(self._image, self.default_command, detach=True)


@pytest.fixture(scope='module')
def docker_container(container_image):
    docker_container = DockerContainer(container_image)
    docker_container.run()
    yield docker_container
    docker_container.kill()