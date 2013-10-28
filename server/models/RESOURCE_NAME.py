""" TODO: Add model code for your resource here.
You'll want to change the file name to whatever your resource is called.
To add persistence to your models, use App Engine's Datastore if you anticipate
scaling to a high amount of data or traffic. The Python NDB module adds caching
and some other features to Datastore.  Consider Google CloudSQL if you
need a relational database.
"""

class RESOURCE_NAME(object):

  @classmethod
  def find(cls, key):
    """ Return a RESOURCE_NAME with key

    Arg: key is a key used to fetch the resource object

    TODO: replace with a query using Datastore or CloudSQL
    """
    result = cls()
    result.answer = '42'
    return result
