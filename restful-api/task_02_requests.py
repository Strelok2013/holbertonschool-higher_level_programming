#!/usr/bin/python3
""""""
import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    json_data = r.json()
    print(r)
    for i in range(len(json_data)):
        print(json_data[i]['title'])

def fetch_and_save_posts():
    # key value pairs to pull:
    # userID : int
    # id : int
    # title: str
    # body: str
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    json_data = r.json()
    list = [i for i in json_data]
    with open("posts.csv", 'w', newline='')as f:
        names = ['id', 'title' , 'body']
        writer = csv.DictWriter(f, fieldnames=names, quotechar= '"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for i in list:
            e = {"id": i['id'], "title": i['title'], "body": i['body'].replace("\n", " ")}
            writer.writerow(e)
fetch_and_print_posts()
fetch_and_save_posts()