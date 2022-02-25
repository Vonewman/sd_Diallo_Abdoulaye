import csv
import json
import yaml
from json import load
from json import loads
from json import dumps
from yaml import safe_load
from dicttoxml import dicttoxml as dtx


def dict2file(data, fname, extent):
    with open(f'{fname}.{extent}', 'w') as f:
        if extent == 'csv':
            data = [data]
            fieldnames = data[0].keys()
            csvfile = csv.DictWriter(f, fieldnames)
            csvfile.writeheader()
            for x in data:
                csvfile.writerow(x)
        elif extent == "json":
            json.dump(dumps(data), f)
        elif extent == "xml":
            xmlfile = dtx(data)
            f.write(str(xmlfile, "utf-8"))
        elif extent == "yaml" or extent == "yml":
            yaml.dump(data, f)
        else:
            print("This file format is not supported !!!")

    print(f"{fname}.{extent} is successfully created!!!")
