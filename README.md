Asko-cli
========

asko-cli provide python scripts to:

- Integrate datasets into a distant [AskOmics](https://github.com/askomics/askomics)
- Launch a query into a distant [AskOmics](https://github.com/askomics/askomics) and get the results (TODO)



Integration
-----------

General options:

- -h, --help: display this help
- -a, --askomics: url of your distant askomics
- -p, --port: the port of your distant askomics
- -u, --user: your askomics username
- -k, --apikey: your askomics apikey
- -d, --data: path of the file to integrate

GFF options:

- -e, --entities: entities to integrate (separated with coma ',')
- -t, --taxon: the taxon

Exemple

    python3 integrate-cli.py -a http://localhost -p 6543 -u myusername -k mYap1keY -d /path/to/file.tsv
    python3 integrate-cli.py -a http://localhost -p 6543 -u myusername -k mYap1keY -d /path/to/file.gff -e transcript,gene,miRNA -t Arabidopsis_thaliana
    python3 integrate-cli.py -a http://localhost -p 6543 -u myusername -k mYap1keY -d /path/to/file.ttl





TODO
----

- [x] Use a apikey instead of the user password
- [ ] Query script