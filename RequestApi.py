"""This module contain the requestApi class
to communicate with the AskOmics API"""

import os
from os.path import basename 
import requests
import json

class RequestApi():
    """RequestApi contain method to communicate with
    the AskOmics API"""


    def __init__(self, url, username, apikey):

        self.url = url
        self.cookies = None
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}
        self.username = username
        self.apikey = apikey
        self.col_types = None
        self.key_columns = [0] # Default value
        self.path = None

    def set_cookie(self):
        """set the session cookie of user
        
        [description]
        :param username: username
        :type username: string
        :param apikey: apikey of username
        :type apikey: string
        :returns: session cookie of username
        :rtype: cookies
        """


        json_dict = {
            'username_email': self.username,
            'password': self.apikey
        }

        url = self.url + '/login'

        try:
            response = requests.post(url, json=json_dict)
        except Exception as exc:
            print('Error: ' + str(exc))

        # Check the passwd
        if 'error' in json.loads(response.text):
            print('Error:\n' + '\n'.join(json.loads(response.text)['error']))

        cookies = response.cookies

        self.cookies = cookies

    def upload_file(self):
        """Upload a file into tmp dir of user
        
        [description]
        :returns: the response dict
        :rtype: dict
        """

        url = self.url + '/up/file'
        files = {
            basename(self.path): open(self.path, 'rb')
        }

        response = requests.post(url, files=files, cookies=self.cookies, headers=self.headers)

        if 'error' in json.loads(response.text):
            print('Error:\n' + json.loads(response.text)['error'])

        return response.text

    def set_key_columns(self, keycols):
        """Set the key columns

        [description]
        :param keycols: list of key index
        :type keycols: list
        """

        self.key_columns = keycols

    def set_filepath(self, path):
        """set the file path"""

        self.path = path

    def guess_col_types(self):
        """Guess the colomns type of a csv file"""

        url = self.url + '/guess_csv_header_type'

        json_dict = {
            'filename': basename(self.path)
        }

        response = requests.post(url, cookies=self.cookies, headers=self.headers, json=json_dict)

        if 'error' in json.loads(response.text):
            print('Error:\n' + json.loads(response.text)['error'])


        self.col_types = json.loads(response.text)['types']
        self.col_types[0] = 'entity_start'


    def integrate_data(self):
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


        json_dict = {
            'file_name': os.path.splitext(basename(self.path))[0],
            'col_types': self.col_types,
            'disabled_columns': [],
            'key_columns': self.key_columns,
            'public': False
        }

        response = requests.post(url, cookies=self.cookies, headers=self.headers, json=json_dict)

        if 'error' in json.loads(response.text):
            print('Error:\n' + json.loads(response.text)['error'])

        return response.text
