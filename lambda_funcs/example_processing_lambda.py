import os
import logging
import json
from typing import Tuple
from urllib.parse import unquote_plus
import boto3
from io import BytesIO

client = boto3.client("s3")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
INPUT_BUCKET = os.environ["input_bucket"]
OUTPUT_BUCKET = os.environ["output_bucket"]


def get_object_from_input_bucket(event: dict) -> Tuple:
    file_obj = event["Records"][0]
    bucket_name = str(file_obj["s3"]["bucket"]["name"])
    key = unquote_plus(str(file_obj["s3"]["object"]["key"]))
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket_name, key)
    s3_file_obj = obj.get()["Body"].read()
    return (key, s3_file_obj)


def save_object_to_output_bucket(key, obj):
    bytes_ = BytesIO(obj)
    client.put_object(Body=bytes_, Bucket=OUTPUT_BUCKET, Key=key)


def lambda_handler(event: dict, _context) -> str:
    # Always nice to dump the event into logs.
    logger.info(f"Initial event in lambda_handler: {json.dumps(event)}")
    # From the event package we can find the uploaded file key and download it.
    key, s3_file_obj = get_object_from_input_bucket(event=event)
    # Now we can save that object to our output bucket.
    save_object_to_output_bucket(key=key, obj=s3_file_obj)
    return (
        f"Input data {key} from {INPUT_BUCKET}. Outputting to {OUTPUT_BUCKET}"
    )
