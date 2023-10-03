import requests
import base64
import os
from fastapi.exceptions import HTTPException

class HiboutikApi:
    _username = os.environ.get('HIBOUTIK_API_USERNAME')
    _token = os.environ.get('HIBOUTIK_API_TOKEN')
    _url = os.environ.get('HIBOUTIK_API_URL')

    @classmethod
    def __get_auth_header(cls):
        if cls._username is None or cls._token is None or cls._url is None:
            raise HTTPException(status_code=500, detail="Internal Server Error")
        base64string = base64.b64encode(bytes('%s:%s' % (cls._username, cls._token), 'ascii'))
        header = "Basic %s" % base64string.decode('utf-8')
        return {'Authorization': header}

    @classmethod
    def get(cls, path, params=None):
        if (header := cls.__get_auth_header()) is not None:
            r = requests.get(cls._url + path, params=params, headers=cls.__get_auth_header())
        return r

    @classmethod
    def post(cls, path, data):
        if (header := cls.__get_auth_header()) is not None:
            r = requests.post(cls._url + path, data=data, headers=cls.__get_auth_header())
        return r
    
    @classmethod
    def put(cls, path, data):
        if (header := cls.__get_auth_header()) is not None:
            r = requests.put(cls._url + path, data=data, headers=cls.__get_auth_header())
        return r

    @classmethod
    def delete(cls, path):
        if (header := cls.__get_auth_header()) is not None:
            r = requests.delete(cls._url + path, headers=cls.__get_auth_header())
        return r
    
    # Methods not implemented :
    # Head, Connect, Options, Trace