###  Add the Jinja2 templating language ###

# Jinja2 is included in app engine SDK so doesn't need to be included here
import jinja2

# configure the Jinja2 templating library to read templates under server/views
JINJA_ENV = jinja2.Environment(
    # path is relative to top level project
    loader=jinja2.FileSystemLoader('server/views'),
    extensions=['jinja2.ext.autoescape'])


### Add custom jinja filters below ###
def please_format(value):
  """Prepend 'please do' to value. """
  return u'please give me %s' % value

JINJA_ENV.filters['sayplease'] = please_format
