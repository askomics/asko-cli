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

        :returns: session cookie of username
        :rtype: cookies
        """


        json_dict = {
            'username': self.username,
            'apikey': self.apikey
        }

        url = self.url + '/login_api'

        try:
            response = requests.post(url, json=json_dict)
        except Exception as exc:
            print('Error: ' + str(exc))

        # print(response.text)

        # Check the passwd
        if 'error' in json.loads(response.text):
            if json.loads(response.text)['error']:
                print('Error:\n' + '\n'.join(json.loads(response.text)['error']))

        cookies = response.cookies

        self.cookies = cookies

    def upload_file(self):
        """Upload a file into tmp dir of user

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
            'filename': os.path.splitext(basename(self.path))[0]
        }

        response = requests.post(url, cookies=self.cookies, headers=self.headers, json=json_dict)

        if 'error' in json.loads(response.text):
            print('Error:\n' + json.loads(response.text)['error'])


        self.col_types = json.loads(response.text)['types']
        self.col_types[0] = 'entity_start'


    def integrate_data(self):
        """Integrate the csv file into the triplestore

        :returns: response text
        :rtype: string
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
