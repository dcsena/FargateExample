import logging
import os
import json
import decimal
from test_handler import test

stage = os.environ["STAGE"]

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


def get_response(status_code, body=None):
    return {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "body": json.dumps(body, default=decimal_default)
    }


def route_api(event):
    logger.debug("Incoming request: {}".format(json.dumps(event)))
    request_context = event['requestContext']
    path = request_context['resourcePath']
    body = json.loads(event['body']) if "body" in event and event["body"] else None
    query = event["queryStringParameters"]
    http_method = request_context['httpMethod']
    try:
        if http_method == "POST":
            if path == "/test":
                result = test(body)
                return get_response(200, result)
    except Exception as ex:
        logger.error("ERROR", exc_info=True, stack_info=True)
        return get_response(500, {"message": str(ex)})


def lambda_handler(event, context):
    logger.debug("Event %s", json.dumps(event))
    return route_api(event)
