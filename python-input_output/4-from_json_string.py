#!/usr/bin/python3
import json
""""""


def from_json_string(my_str):
    """"""
    return json.loads(my_str)

obj = from_json_string('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(obj)
print(type(obj))