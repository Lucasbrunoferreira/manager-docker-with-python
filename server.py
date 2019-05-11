from flask import Flask, request, abort, jsonify
from docker_client import DockerClient

import json


app = Flask(__name__)

docker = DockerClient()


@app.route("/docker/image/pull", methods=["POST"])
def image_pull():
    try:
        docker_img = json.loads(request.data).get("docker_img")
        image_tag = json.loads(request.data).get("image_tag")

        image = docker.pull_docker_image(docker_img, image_tag)
        return jsonify({
            "message": "the image: {}:{} has been updated".format(docker_img, image_tag),
            "image_id": image.id
        })

    except Exception as ex:
        print(ex)
        abort(status=500)


@app.route("/docker/container/update", methods=["POST"])
def update_container():
    try:
        container_name = json.loads(request.data).get("container_name")
        image_tag = json.loads(request.data).get("image_tag")

        container = docker.update_container(container_name, image_tag)
        return jsonify({
            "message": "the container: {}:{} has been updated".format(container_name, image_tag),
            "container_id": container.id
        })

    except Exception as ex:
        print(ex)
        abort(status=500)


@app.route("/docker/container/run", methods=["POST"])
def container_run():
    try:
        docker_img = json.loads(request.data).get("docker_img")
        container_name = json.loads(request.data).get("container_name")

        container = docker.run_container(docker_img, container_name)
        return jsonify({
            "message": "the {} container is running".format(container_name),
            "container_id": container.id
        })

    except Exception as ex:
        print(ex)
        abort(status=500)


@app.route("/docker/container/remove", methods=["POST"])
def remove_container():
    try:
        container_name = json.loads(request.data).get("container_name")

        docker.remove_container(container_name)
        return jsonify({
            "message": "the {} container has been removed".format(container_name)
        })

    except Exception as ex:
        print(ex)
        abort(status=500)


if __name__ == '__main__':
    app.run(debug=False, port=8000)
