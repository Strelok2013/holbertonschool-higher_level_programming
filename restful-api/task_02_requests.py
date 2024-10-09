#!/usr/bin/python3
""""""
import requests
import json

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com')
    ##json_data = r.json()
    print(r)

fetch_and_print_posts()