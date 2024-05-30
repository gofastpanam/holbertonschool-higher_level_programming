#!/usr/bin/python3
"""
Rreading data from one format (CSV)
and converting it into another format (JSON)
using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
      try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent='4')

        return True
      except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
