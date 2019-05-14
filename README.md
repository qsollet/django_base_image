# Ocean Core Infrastructure Django Base

## How to use

### Build your project

In your `Dockerfile` just use this:

```
FROM django_base_image:latest
```

You will need to have a `requirements.txt` file with all you dependency.

If you need to run some scripts while building you can use `pre-build` and/or `pre-run`.

### Run tests

```
docker run -it $(IMAGE_TAG) test-django
```

If you need to set any environment variable use the `test.env` file.

### Deploy

Mount static volume for Nginx to serve on `/static`

## Env

- GUNICORN_BIND_IP | 0.0.0.0
- GUNICORN_BIND_PORT | 80
- GUNICORN_WORKER | 2
