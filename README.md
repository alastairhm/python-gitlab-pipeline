# Dynamic Pipeline Generation Script

Small POC using Python and Jinja2 templates to generate Gitlab pipelines dynamically.

## Example generating rules for multiple environments

Uses `templates/rule.yml` template to generate the rules depending on what environemnts are passed.

```bash
 ./generate_rules.py generate --filename=test.yml --environments="sandbox,dev,qa" -template_file="rule.yml"
 ```

```bash
./generate_rules.py
NAME
    generate_rules.py - Generate Pipeline YAML from a template

SYNOPSIS
    generate_rules.py - GROUP | COMMAND | VALUE

DESCRIPTION
    Generate Pipeline YAML from a template

GROUPS
    GROUP is one of the following:

     environment
       The core component of Jinja is the `Environment`.  It contains important shared variables like configuration, filters, tests, globals and others.  Instances of this class may be modified if they are not shared and if no template was loaded so far. Modifications on environments after the first template was loaded will lead to surprising effects and undefined behavior.

COMMANDS
    COMMAND is one of the following:

     dump
       Info Dump

     generate
       Generate Gitlab Pipeline file from template

VALUES
    VALUE is one of the following:

     template_dir

     template_file
```
