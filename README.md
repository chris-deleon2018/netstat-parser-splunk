# Netstat (Linux) Parser Splunk
The python script is a work in progress, but the intention is to create run a netstat -antup on a Linux machine and parse the results. The results are formatted as JSON and saved to a file. The file will then be ingested into Splunk.

## How to run
```
python3 netstat_parser.py
```
