import requests
import base64
import os

class HiboutikApi:
    _username = os.environ.get('HIBOUTIK_API_USERNAME')
    _token = os.environ.get('HIBOUTIK_API_TOKEN')
    _url = os.environ.get('HIBOUTIK_API_URL')

    @classmethod
    def __get_auth_header(cls):
        if cls._username is None or cls._token is None or cls._url is None:
            raise Exception('HiboutikApi: missing environment variables')
        base64string = base64.b64encode(bytes('%s:%s' % (cls._username, cls._token), 'ascii'))
        header = "Basic %s" % base64string.decode('utf-8')
        return {'Authorization': header}

    @classmethod
    def get(cls, path, params=None):
        r = requests.get(cls._url + path, params=params, headers=cls.__get_auth_header())
        return r

    @classmethod
    def post(cls, path, data):
        r = requests.post(cls._url + path, data=data, headers=cls.__get_auth_header())
        return r
    
    @classmethod
    def put(cls, path, data):
        r = requests.put(cls._url + path, data=data, headers=cls.__get_auth_header())
        return r

    @classmethod
    def delete(cls, path):
        r = requests.delete(cls._url + path, headers=cls.__get_auth_header())
        return r
    
    # Methods not implemented :
    # Head, Connect, Options, Trace