import json
from pprint import pprint

# read file
with open('volumes.json') as myfile:
    data=myfile.read()

pprint(data)