#!/usr/bin/env python
import os
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput


class OutputStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here

        TerraformOutput(self, 'OutputStack', value=12)


app = App()
OutputStack(app, "cdktf-python")
app.synth()