# Ocean Core Infrastructure Django Base

## How to use

### Build your project

In your `Dockerfile` just use this:

```
FROM django_base_image:latest
```

You will need to have a `requirements.txt` file with all you dependency

If you need to run some scripts while building

### Run tests

`docker run -it $(IMAGE_TAG) test-django`

### Deploy

Set panda auth
mount static volume for Nginx to serve on `/static`

## Env

- GUNICORN_BIND_IP | 0.0.0.0
- GUNICORN_BIND_PORT | 80
- GUNICORN_WORKER | 2
- DJANGO_SECRET_KEY | random string
- DJANGO_STATIC_ROOT | '/static'
- DJANGO_MEDIA_ROOT | '/media'
- DJANGO_DEBUG | False
- DJANGO_APP_NAME | app name
- DJANGO_DB_ENGINE | 'django.db.backends.postgresql'
- DJANGO_DB_NAME | app name
- DJANGO_DB_USER | app name
- DJANGO_DB_PASSWORD | 'password'
- DJANGO_DB_HOST | 'database'
- DJANGO_DB_PORT | 5432

## TODOs

- add `pre-build` and `pre-run` scripts
- add PEP8 to tests (with longer lines)
- add cron import if `cronjob` file exists
