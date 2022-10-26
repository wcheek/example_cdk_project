import aws_cdk as core
import aws_cdk.assertions as assertions

from example_cdk_project.example_cdk_project_stack import ExampleCdkProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in example_cdk_project/example_cdk_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ExampleCdkProjectStack(app, "example-cdk-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
