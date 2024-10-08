#!/usr/bin/python3
import json
import csv
""""""


def convert_csv_to_json(filename):
    """"""
    try:
        with open(filename, 'r') as f:
            data = []
            for r in csv.DictReader(f):
                data.append(r)

        with open ("data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except FileNotFoundError:
        print("File not found")
        return False
    
csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")