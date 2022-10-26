import aws_cdk as cdk

# * Import your stacks
from example_cdk_project.example_cdk_project_stack import ExampleCdkProjectStack

# * Initialize your cdk app
app = cdk.App()

# * Initialize your stacks
ExampleCdkProjectStack(app, "ExampleCdkProjectStack")

# * synth the stacks - turn CDK code into CloudFormation
app.synth()
