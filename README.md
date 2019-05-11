# Manager Docker Server with Python SDK

API HTTP to manipulate images and container of a server with Docker


### Prerequisites

On your server you need to have installed: Python3, Docker and git.


### Installing

* clone the repository in your server
* `pip install -r requiremetns.txt`
* `python server.py`


## Usage

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
http://yourhost.com/docker/image/pull
body: { "docker_img", "image_tag }

http://yourhost.com/docker/container/update
body: { "container_name", "image_tag }

http://yourhost.com/docker/container/run
body: { "docker_img", "container_name }

http://yourhost.com/docker/container/remove
body: { "container_name }
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Authors

[Lucas Bruno Ferreira](https://github.com/lucasbrunoferreira)

## License

This project is licensed under the MIT License

