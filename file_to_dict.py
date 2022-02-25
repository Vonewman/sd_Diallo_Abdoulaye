import csv
import json
import yaml
from json import load
from json import loads
from json import dumps
from yaml import safe_load
from xmltodict import parse

def file2dict(file_name):
    """Transform a file to dictionary

    Args:
        file_name (str): the file name

    Returns:
        str: returns a strings of dict.
    """
    string = ""
    with open(file_name, 'r') as f:
        if file_name.endswith(".csv"):
            arr = []
            k = 0
            string = csv.DictReader(f)

            for x in string:
                arr.append(x)
            string = arr
        elif file_name.endswith(".json"):
            string = json.load(f)
        elif file_name.endswith(".xml"):
            string = loads(dumps(parse(f.read())))
        elif file_name.endswith(".yaml") or file_name.endswith(".yml"):
            string = safe_load(f)

        return string