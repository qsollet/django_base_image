# Django base image

## How to use

1. Build this image locally
```
docker build -t django_base_image .
```

2. In your Django project `Dockerfile` use it as a base image:
```
FROM django_base_image:latest
```

## Requirements

You will need to have a `requirements.txt` file at the same level as your `Dockerfile` with all you dependency.

To run scripts while building the docker image you can add bash command in `pre-build`.
To run scripts before starting Django use `pre-run`.
They will both run as the `appuser` user.

If you need to add some cronjob add them in a `cronjob` file.

## Run tests

To run Django test from your docker image run:
```
docker run --rm -it $(IMAGE_TAG) test-django
```

If you need to set any environment variable use the `test.env` file.

## Deploy

Mount static volume for Nginx to serve on `/home/appuser/static`.

## Environment variable available

- GUNICORN_BIND_IP (default to `0.0.0.0`)
- GUNICORN_BIND_PORT (default to `80`)
- GUNICORN_WORKER (default to `2`)
