Askocli
========

AskOcli allow an [AskOmics](https://github.com/askomics/askomics) user to integrate file with the command line into a distant [AskOmics](https://github.com/askomics/askomics).

Requirment
----------

- python3
- python3-venv

Installation
------------

Clone the repository

    git clone https://github.com/askomics/asko-cli.git
    cd asko-cli

Set up a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

Install the script in the virtual environment:

    python3 setup.py install

Usage example
-------------

Integration

    askocli integrate -a http://localhost -p 6543 -k mYap1Key path/to/file.csv
    askocli integrate -a http://localhost -p 6543 -k mYap1Key path/to/file.csv
    askocli integrate -a http://localhost -p 6543 -k mYap1Key -e gene transcript -t Arabidopsis_thaliana path/to/file.gff
    askocli integrate -a http://localhost -p 6543 -k mYap1Key path/to/file.ttl


History
-------

- 0.1: Initial release!
    - Integrate CSV file into a distant AskOmics
- 0.2: 
   - Use API key instead of password
   - Integrate GFF and TTL
- 0.3: APIkey
   - Use only the API key without the username to login
   - Better error managment
