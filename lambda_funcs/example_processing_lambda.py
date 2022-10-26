import os
import logging
import json
from typing import Tuple
from urllib.parse import unquote_plus
import boto3
from io import BytesIO

client = boto3.client("s3")
s3_resource = boto3.resource("s3")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
INPUT_BUCKET = os.environ["input_bucket"]
OUTPUT_BUCKET = os.environ["output_bucket"]


def get_object_from_input_bucket(event: dict) -> Tuple:
    # Get JSON record of uploaded file
    file_obj = event["Records"][0]
    # Get the plain text key of file obj.
    key = unquote_plus(str(file_obj["s3"]["object"]["key"]))
    bucket_name = str(file_obj["s3"]["bucket"]["name"])
    obj = s3_resource.Object(bucket_name, key)
    s3_file_obj = obj.get()["Body"].read()
    return (key, s3_file_obj)


def save_object_to_output_bucket(key, obj):
    bytes_ = BytesIO(obj)
    client.put_object(Body=bytes_, Bucket=OUTPUT_BUCKET, Key=key)
    return True


def lambda_handler(event: dict, _context) -> bool:
    # Always nice to dump the event into logs.
    logger.info(f"Initial event in lambda_handler: {json.dumps(event)}")
    # From the event package we can find the uploaded file key and download it.
    key, s3_file_obj = get_object_from_input_bucket(event=event)
    # Now we can save that object to our output bucket.
    save_object_to_output_bucket(key=key, obj=s3_file_obj)
    # Report that it got done.
    logger.info(
        f"Input data {key} from {INPUT_BUCKET}. Outputting to {OUTPUT_BUCKET}"
    )
    return True
