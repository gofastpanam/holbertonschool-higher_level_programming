#!/usr/bin/python3

print(' ------------------------------------------------- ')
print(' ------posts_from_JSONPlaceholder.txt------------- ')
print(' ------------------------------------------------- ')

with open('posts_from_JSONPlaceholder.txt', 'r') as file:
    for line in file:
        print(line.strip())

print(' ------------------------------------------------- ')
print(' ----posts_headers_from_JSONPlaceholder.txt------- ')
print(' ------------------------------------------------- ')

with open('posts_headers_from_JSONPlaceholder.txt', 'r') as file:
    for line in file:
        print(line.strip())

print(' ------------------------------------------------- ')
print(' ----post_request_to_JSONPlaceholder.txt---------- ')
print(' ------------------------------------------------- ')

with open('post_request_to_JSONPlaceholder.txt', 'r') as file:
    for line in file:
        print(line.strip())
