from invoke import task

@task
def start(ctx):
    '''starting the app with poetry run invoke start'''
    ctx.run("python3 src/index.py")

@task
def build(ctx):
    '''creating the necessary databases with poetry run invoke build'''
    ctx.run("python3 src/build.py")

@task
def test(ctx):
    '''testing using pytest with poetry run invoke test'''
    ctx.run("pytest src")

@task
def coverage(ctx):
    '''getting the coverage with poetry run invoke coverage'''
    ctx.run("coverage run --branch -m pytest src")

@task()
def coverage_report(ctx):
    '''getting the coverage with poetry run invoke coverage_report'''
    ctx.run("coverage html")

@task()
def lint(ctx):
    '''getting pylint results with poetry run invoke lint'''
    ctx.run("pylint src")
    