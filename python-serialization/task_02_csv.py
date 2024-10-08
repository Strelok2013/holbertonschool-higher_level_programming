#!/usr/bin/python3
import json
import csv
import sys
""""""


def convert_csv_to_json(filename):
    """"""
    if not filename:
        print("Invalid file name")
        sys.exit()

    try:
        with open(filename, 'r') as f:
            data = []
            for r in csv.DictReader(f):
                data.append(r)

        with open ("data.json", 'w') as f:
            json.dump(data, f)
    except FileNotFoundError:
        print("File not found")
        return False
    return True