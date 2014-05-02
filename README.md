Sandō
=====

A script to apply a source context and/or OS environment variables to Jinja 2 templates.

To generate a new config based on a template using a JSON context:

`python sando.py -i examples/nginx.conf.tmpl -c examples/services.ctx`

Another example using only OS environment variables:

`python sando.py -i examples/my.properties`
