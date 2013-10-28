"""Controller handles routes starting with /RESOURCE_NAME.

Change this file's name and contents as appropriate to the
resources your app exposes to clients.

"""
from server.lib.bottle import Bottle, debug
# use the Jinja templating system
from view_helper import JINJA_ENV
# import model code
from server.models.RESOURCE_NAME import RESOURCE_NAME

bottle = Bottle() # create another WSGI application for this controller and resource.
# debug(True) #  uncomment for verbose error logging. Do not use in production


@bottle.get('/<key>')
def show(key='1'):
  """Display a RESOURCE_NAME with "<key>" if request is to
  /RESOURCE_NAME/<key>.

  Args:
    <key> is interpreted as relative to /RESOURCE_NAME due to mount in main.py
    If no key is specified the default is '1'

  """
  resource = RESOURCE_NAME.find(key)
  return JINJA_ENV.get_template('show.html').render({
      'value': resource.answer
      })
