import sys
import argparse
import json
import os
from jinja2 import Template

def main(argv=None):
    """Command-line tool to apply  a source context and/or OS environment variables to Jinja 2 templates.
    -h
    """
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(description="Command-line tool to apply  a source context and/or OS environment variables to Jinja 2 templates.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=True, help='the input source template')
    parser.add_argument('-c', '--context', required=False, help='context to use for template rendering')
    parser.add_argument('-o', '--output', required=False, help='the output rendered template (optional)')
    args = parser.parse_args()

    with open(args.input, "r") as input_file:
        source_template = input_file.read()
        ctx = {}
        if args.context:
        	with open(args.context, "r") as context_file:
        		ctx = json.loads(context_file.read())
        ctx["os"] = os.environ
        template = Template(source_template)
        print(template.render(**ctx))

if __name__ == "__main__":
    sys.exit(main())
