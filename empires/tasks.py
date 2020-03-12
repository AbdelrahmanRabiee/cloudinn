from celery.decorators import task

@task(name="hello_world")
def hello():
    return 'Hello World'