import boto3
import logging
import os

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stage = os.environ['STAGE']

CONTAINER_NAME = 'FargateExample'
CLUSTER_NAME = 'FargateExample'
SUBNET_ID = ''  # redacted


def run_fargate_task():
    ecs_client = boto3.client('ecs')
    ecs_client.run_task(
        cluster=CLUSTER_NAME,
        taskDefinition=CONTAINER_NAME,
        count=1,
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'assignPublicIp': 'DISABLED',
                'subnets': [SUBNET_ID]
            }
        },
        overrides={
            'containerOverrides': [{
                'name': CONTAINER_NAME,
                'command': [
                    '--script',
                    'test_script',
                    '--stage',
                    stage.upper(),
                    '--write'
                ]
            }]
        }
    )


def test(request):
    run_fargate_task()
