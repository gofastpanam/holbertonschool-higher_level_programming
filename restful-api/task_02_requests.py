#!/usr/bin/python3
"""
This module consuming and processing data from an API using Python
"""

import requests
import csv


def fetch_and_print_posts():
    """
    function that fetches all post from JSONPlaceholder.
    """
    all_post = requests.get("https://jsonplaceholder.typicode.com/posts")
    code = all_post.status_code
    print("Status Code: {}".format(code))

    if code == 200:
        data = all_post.json()
        for item in data:
            print(item["title"])


def fetch_and_save_posts():
    """
    function that fetches all post from JSONPlaceholder and saved in posts.csv
    """
    all_post = requests.get("https://jsonplaceholder.typicode.com/posts")
    code = all_post.status_code

    results = []

    if code == 200:
        data = all_post.json()

        for item in data:
            item_dict = {}

            for key, value in item.items():
                item_dict["id"] = item.get("id")
                item_dict["title"] = item.get("title")
                item_dict["body"] = item.get("body")
            results.append(item_dict)

        with open("posts.csv", "w") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
