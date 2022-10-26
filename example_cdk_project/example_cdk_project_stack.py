from aws_cdk import Stack, Duration
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_lambda as _lambda
from constructs import Construct


class ExampleCdkProjectStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        input_bucket = s3.Bucket(scope=self, id="inputBucket")
        output_bucket = s3.Bucket(scope=self, id="outputBucket")

        processing_lambda = _lambda.Function(
            scope=self,
            id="processingLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            # Path is relative to where I execute cdk
            code=_lambda.Code.from_asset(
                path="lambda_funcs"
            ),
            handler="example_processing_lambda.lambda_handler",
            environment={
                "input_bucket": input_bucket.bucket_name,
                "output_bucket": output_bucket.bucket_name,
            },
            timeout=Duration.seconds(45),
            description="Example processing lambda function.",
        )
