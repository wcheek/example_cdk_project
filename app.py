#!/usr/bin/env python3
import os

import aws_cdk as cdk

from example_cdk_project.example_cdk_project_stack import ExampleCdkProjectStack


app = cdk.App()
ExampleCdkProjectStack(app, "ExampleCdkProjectStack")

app.synth()
