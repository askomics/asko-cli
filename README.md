Asko-cli
========

asko-cli provide python scripts to:

- Integrate datasets into a distant [AskOmics](https://github.com/askomics/askomics)
- Launch a query (json formatted) into a distant [AskOmics](https://github.com/askomics/askomics) and get the results (TODO)

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

    askocli integrate -a http://localhost -p 6543 -u username -k mYap1Key path/to/file.csv
    askocli integrate -a http://localhost -p 6543 -u username -k mYap1Key path/to/file.csv
    askocli integrate -a http://localhost -p 6543 -u username -k mYap1Key -e gene transcript -t Arabidopsis_thaliana path/to/file.gff
    askocli integrate -a http://localhost -p 6543 -u username -k mYap1Key path/to/file.ttl

TODO
----

- [ ] Query script
- [ ] Better error managment