# RESTful API

## 0. Basics of HTTP/HTTPS

task_00_http_https.txt

## 1. Consume data from an API using command line tools (curl)

curl https://jsonplaceholder.typicode.com/posts > posts_from_JSONPlaceholder.txt

curl -I https://jsonplaceholder.typicode.com/posts > posts_headers_from_JSONPlaceholder.txt

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts > post_request_to_JSONPlaceholder.txt

task_01_curl.py

## 2. Consuming and processing data from an API using Python

task_02_requests.py

## 3. Develop a simple API using Python with the `http.server` module

task_03_http_server.py