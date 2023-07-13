#!/usr/bin/env python
import json, glob
from os import getenv
from json import dumps
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_datadog import dashboard_json
from cdktf_cdktf_provider_datadog.provider import DatadogProvider


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        provider = DatadogProvider(self,
                            'provider',
                            api_url='https://api.datadoghq.eu/',
                            api_key=getenv('DATADOG_API_URL'),
                            app_key=getenv('DATADOG_APP_URL')
                            )

        # define resources here

        json_dash_model = []

        for file in glob.glob("dash_*.json"):
            try:
                with open(file, "r", encoding='utf-8') as infile:
                    file_content = json.load(infile)
                    json_dash_model.append(file_content)
            except json.JSONDecodeError as error:
                print(f"Error {file}: {error}")

        all_items = []
        for json_file in json_dash_model:
            #all_items += json_file['widgets']
            all_items.extend(json_file['widgets'])

        final_json = {}
        final_json['title'] = "cvetkovska-cdk-dash"
        final_json['layout_type'] = "ordered"
        final_json['widgets'] = all_items

        with open("merged_file.json", "w", encoding='utf-8') as outfile:
            #json.dump({"widgets": all_items}, outfile, ensure_ascii=False, indent=4)
            json.dump(final_json, outfile, ensure_ascii=False, indent=4)

        dashboard = ' '

        for line in glob.glob("merged_file.json"):
            with open(line, "r", encoding='utf-8') as dash:
                dash_content = json.load(dash)
                dashboard = dumps(dash_content)

        dashboard_json.DashboardJson(
            self,
            'cvetkovska_dashboard_cdk',
            dashboard=dashboard,
            provider=provider,
        )

app = App()
MyStack(app, "cdktf-python")

app.synth()
