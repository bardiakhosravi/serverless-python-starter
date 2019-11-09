from invoke import task


def sls(stage=None, aws_profile=None, command=""):
    cmd = f"serverless {command} -s {stage}"
    if aws_profile is not None:
        cmd += f" --aws-profile {aws_profile}"

    return cmd


@task
def deploy(c, stage="dev", aws_profile=None):
    c.run(sls(stage, aws_profile, "deploy"))


@task
def remove(c, stage="dev", aws_profile=None):
    c.run(sls(stage, aws_profile, "remove"))



