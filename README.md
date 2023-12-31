# OpenAPI generated server

## Overview
This server was generated by the [OpenAPI Generator](https://openapi-generator.tech) project. By using the
[OpenAPI-Spec](https://openapis.org) from a remote server, you can easily generate a server stub.  This
is an example of building a OpenAPI-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m mr
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8080/openapi.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t mr .

# starting up a container
docker run -p 8080:8080 mr
```

## Development


### Regenerate Server

Install `openapi-generator-cli` following these [instructions](https://github.com/OpenAPITools/openapi-generator/#launcher-script).

From the root of the directory run the following command:

```bash
$ openapi-generator-cli generate -i openapi/openapi.yaml -g python-flask -o . --package-name mr
```

> **NOTE**: running the previous command you will regenerate `/mr/controllers`, `/mr/models` and `/mr/openapi`

### Check OpenAPI

Run OpenAPI specifications directly even before any operation handler function gets implemented. This allows you to verify and inspect how your API will work with Connexion.

```bash
$ connexion run server/openapi/openapi.yaml --stub --debug
```

### Running Mock Server

You can run a simple server which returns example responses on every request. The example responses must be defined in the examples response property of the OpenAPI specification. Your API specification file is not required to have any operationId.

```bash
$ connexion run server/openapi/openapi.yaml --mock=all -v
```
