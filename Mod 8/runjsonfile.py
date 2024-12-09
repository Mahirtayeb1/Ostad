import json
import csv

filename = "jsonsample.json"

with open(filename, mode = "rt") as fp:
    data = json.loads(fp.read())
    print(json.dumps(data, sort_keys=False, indent= 4))
    print(type(data))
    for key, value in data.items():
        print(key, value)