"""Integragte a CSV/TSV file into a distant AskOmics"""

import sys
import os
from os.path import basename 
from lib.RequestApi import RequestApi
from lib.ManageArg import ManageArg

def main():
    """Integragte a CSV/TSV file into a distant AskOmics"""

    manage_arg = ManageArg()
    arg_dict = manage_arg.get_args(sys.argv[1:])

    api = RequestApi(arg_dict['url'], arg_dict['user'], arg_dict['apikey'])

    api.set_cookie()

    api.set_filepath(arg_dict['path'])

    api.upload_file()

    ext = os.path.splitext(basename(arg_dict['path']))[1].lower()

    if ext in ('.gff', '.gff2', '.gff3') or arg_dict['file_type'] == 'gff3':
        api.integrate_gff(arg_dict['taxon'], arg_dict['entities'])
    elif ext == '.ttl' or arg_dict['file_type'] == 'ttl':
        api.integrate_ttl()
    else:
        api.guess_col_types()
        api.integrate_data()


if __name__ == '__main__':
    main()
