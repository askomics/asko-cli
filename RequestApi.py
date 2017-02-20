"""This module contain the requestApi class
to communicate with the AskOmics API"""

import os
from os.path import basename 
import requests

class RequestApi():
    """RequestApi contain method to communicate with
    the AskOmics API"""



    def __init__(self, url):

        self.url = url
        self.cookies = None
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}



    def get_cookie(self, username, apikey):
        """Get the session cookie of user
        
        [description]
        :param username: username
        :type username: string
        :param apikey: apikey of username
        :type apikey: string
        :returns: session cookie of username
        :rtype: cookies
        """


        json = {
            'username_email': username,
            'password': apikey
        }

        url = self.url + '/login'

        response = requests.post(url, json=json)
        cookies = response.cookies

        self.cookies = cookies


    def upload_file(self, path):
        """Upload a file into tmp dir of user
        
        [description]
        :returns: the response dict
        :rtype: dict
        """

        url = self.url + '/up/file'
        files = {
            basename(path): open(path, 'rb')
        }

        response = requests.post(url, files=files, cookies=self.cookies, headers=self.headers)

        return response.text

    def ingtegrate_data(self, path, col_types, key_columns):
        """Integrate the csv file into the triplestore
        
        [description]
        :param path: the path of the file
        :type path: string
        :param col_types: list of columns types
        :type col_types: list
        :param key_columns: the key columns index
        :type key_columns: list
        :returns: response status
        :rtype: dict
        """


        url = self.url + '/load_data_into_graph'


        json = {
            'file_name': os.path.splitext(basename(path))[0],
            'col_types': col_types,
            'disabled_columns': [],
            'key_columns': key_columns,
            'public': False
        }

        response = requests.post(url, cookies=self.cookies, headers=self.headers, json=json)

        return response.text

