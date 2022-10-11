#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ
import fire
from jinja2 import Environment, FileSystemLoader

class Generate:
    """Generate Pipeline YAML from a template"""

    def __init__(self, template_dir="templates/", template_file="rule.yml"):
        """Init"""
        self.template_dir = template_dir
        self.template_file = template_file
        self.environment = Environment(loader=FileSystemLoader(self.template_dir))

    def dump(self):
        """Info Dump"""
        print(self.template_dir)
        print(self.template_file)

    def generate(self, environments , filename="generated_rules.yml"):
        """Generate Gitlab Pipeline file from template"""
        self.template = self.environment.get_template(self.template_file)

        pipeline = ""

        for env in list(environments):
            pipeline = pipeline + self.template.render(deploy_env=env)

        with open(filename, mode="w") as pipe:
            pipe.write(pipeline)

if __name__ == '__main__':

    fire.Fire(Generate)
