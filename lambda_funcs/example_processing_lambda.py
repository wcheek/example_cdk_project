import os
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
INPUT_BUCKET = os.environ["input_bucket"]
OUTPUT_BUCKET = os.environ["output_bucket"]


def lambda_handler(event: dict, _context):
    logger.info(f"Initial event in lambda_handler: {json.dumps(event)}")
    file_name = "example"
    return f"Input data {file_name} from {INPUT_BUCKET}. Outputting to {OUTPUT_BUCKET}"
