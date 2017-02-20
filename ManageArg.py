"""This module contain the class ManageArg"""

import getopt
import sys


class ManageArg():
    """Manage the arguments of asko-cli"""

    def __init__(self):
        pass


    @staticmethod
    def usage():
        """Print the help message"""

        print('Options:')
        print('\t-h, --help: display this help')
        print('\t-a, --askomics: url of your distant askomics')
        print('\t-p, --port: the port of your distant askomics')
        print('\t-u, --user: your askomics username')
        print('\t-k, --apikey: your askomics apikey')
        print('\t-d, --data: path of the file to integrate')

    def get_args(self, argv):
        """Get the arguments of the script
        
        :param argv: the list of arguments
        :type argv: list
        :returns: the parsed arguments
        :rtype: dict
        """

        results = {}

        try:
            opts, argvs = getopt.getopt(
                argv, 'ha:p:u:k:d:',
                ['help=', 'askomics=', 'port=', 'username=', 'data='])
        except getopt.GetoptError:
            self.usage()
            sys.exit(2)
        if not opts:
            self.usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                self.usage()
                sys.exit(2)
            elif opt in ('-a', '--askomics'):
                asko_url = str(arg)
            elif opt in ('-p', '--port'):
                asko_port = str(arg)
            elif opt in ('-u', '--user'):
                username = str(arg)
            elif opt in ('-k', '--apikey'):
                api_key = str(arg)
            elif opt in ('-d', '--data'):
                path = str(arg)

        if not asko_url or not username or not api_key or not path:
            self.usage()
            sys.exit(2)

        if asko_port:
            asko_url = asko_url + ':' + asko_port

        #TODO: Check the server

        #TODO: Check the filepath


        results['url'] = asko_url
        results['user'] = username
        results['apikey'] = api_key
        results['path'] = path

        return results
