# Python Starter For Serverless Framework with AWS

At this point this project deploys A Python3.6 Lambda function on AWS using the following tools:

1. [Serverless framework](https://serverless.com/)
2. `Pipenv` is used for managing the the python environment.
3. [Invoke](http://www.pyinvoke.org/) is used as a task runner.
 

## Requirements

1. Python 3.6
2. [Install serverless framework](https://serverless.com/framework/docs/getting-started/)

## Setup

[Install pipenv](https://pipenv-fork.readthedocs.io/en/latest/)


[Install AWS CLI](https://aws.amazon.com/cli/)

[Configure AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) and 
note the profile you create under ~/.aws/credentials for deployment. 


[Install Docker](https://docs.docker.com/v17.12/docker-for-mac/)

Docker is used by the [serverless-python-requirements serverless](https://github.com/UnitedIncome/serverless-python-requirements) 
plugin for deployment


Create a pipenv environment

`$ pipenv shell`

Set up node packages by running

`$ npm install` on the root of the project.

Install all packages in `Pipfile` (note that you have to be inside the active pipend environment for the project):

`pipenv install invoke`

## Deployment

`tasks.py` contains a set of invoke tasks that wrap the serverless 
framework deployment commands to make it easy to deploy to various stages.
You can extends them, or write your own tasks, or just run serverless
commands from the command line as you prefer. 

e.g. deploy to dev environment

`$ invoke deploy --stage=dev` 

This will deploy to an AWS account using your `[default]`
credentials set in ~/.aws/credentials. If you wish to deploy using a specific profile
use

`$ invoke deploy --stage=dev --aws-profile=<profile name>`

This will deploy all the resources and Lambda functions to AWS.
`Note: Recommendation is to deploy dev and testing environments in a differnet AWS 
account`

Remove your entire stack using

`$ invoke remove --stage=<stage name> --aws-profile=<profile name>`

## Pycharm Setup

If using PyCharm ensure to set the project interpreter to be 
the created virtual environment by pipenv


 