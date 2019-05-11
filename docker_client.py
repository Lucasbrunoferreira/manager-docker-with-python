import docker


class DockerClient:
    def __init__(self):
        self.docker_client = docker.from_env()

    def pull_docker_image(self, image_name, image_tag):
        return self.docker_client.images.pull(repository=image_name, tag=image_tag)

    def update_container(self, container_name, image_tag):
        self.remove_container(container_name)
        self.pull_docker_image(container_name, image_tag)
        return self.run_container(container_name, container_name)

    def run_container(self, docker_img, container_name):
        return self.docker_client.containers.run(image=docker_img, detach=True, name=container_name)

    def remove_container(self, container_name):
        for container in self.docker_client.containers.list(all=True):
            if container.attrs['Name'] == '/{}'.format(container_name):
                container.remove(force=True)
        return

    def remove_all_containers(self):
        for container in self.docker_client.containers.list(all=True):
            container.remove(force=True)
        return

