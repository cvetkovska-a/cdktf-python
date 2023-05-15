#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here

        TerraformOutput(self, "TestStack",value="14")


app = App()
MyStack(app, "cdktf-python")

app.synth()
