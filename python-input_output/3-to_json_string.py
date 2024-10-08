#!/usr/bin/python3
import json
""""""


def to_json_string(my_obj):
    """"""
    return json.dumps(my_obj)

list = [1, 2, 3, 4]

print(to_json_string(['foo', {'bar': ('baz', None, 1.0, 2)}]))