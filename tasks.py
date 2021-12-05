from invoke import task

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src ")
    ctx.run("coverage report -m ")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")