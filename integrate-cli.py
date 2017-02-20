"""Integragte a CSV/TSV file into a distant AskOmics"""

import sys
from RequestApi import RequestApi
from ManageArg import ManageArg

def main():
    """Integragte a CSV/TSV file into a distant AskOmics"""

    manage_arg = ManageArg()
    arg_dict = manage_arg.get_args(sys.argv[1:])

    api = RequestApi(arg_dict['url'], arg_dict['user'], arg_dict['apikey'])

    api.set_cookie()

    api.set_filepath(arg_dict['path'])

    api.upload_file()

    api.guess_col_types()

    api.integrate_data()


if __name__ == '__main__':
    main()
