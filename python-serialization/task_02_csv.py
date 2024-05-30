#!/usr/bin/python3
"""
Rreading data from one format (CSV)
and converting it into another format (JSON)
using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(filename):
    with open(filename, 'r') as file:
        try:
            result = csv.reader(file)
            writer = csv.DictWriter(result)
            json.dumps(data.json, file)
            return True
        except FileNotFoundError:
            return False
