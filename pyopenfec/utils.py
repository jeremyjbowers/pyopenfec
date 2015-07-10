import exceptions
import json
import os

import requests

API_KEY = os.environ.get('OPENFEC_API_KEY', None)
BASE_URL = 'https://api.open.fec.gov'
VERSION = '/v1'

class OpenFecException(exceptions.Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    def __unicode__(self):
        return unicode(self.value)

def make_request(resource, **kwargs):
    url = BASE_URL + VERSION + '/%s' % resource

    if not API_KEY:
        raise OpenFecException('Please export an env var OPENFEC_API_KEY with your API key.')

    params = dict(kwargs)
    params['api_key'] = API_KEY

    r = requests.get(url, params=params)

    if r.status_code != 200:
        raise OpenFecException('OpenFEC site returned a status code of %s for this request.' % r.status_code)

    return r.json()