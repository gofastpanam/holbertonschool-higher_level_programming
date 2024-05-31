#!/usr/bin/python3

def print_stylish_separator(title):
    width = len(title) + 10
    print(f"{'-' * width}")
    print(f"{' ' * 5}{title}")
    print(f"{'-' * width}")

def print_file_content(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

print_stylish_separator("posts_from_JSONPlaceholder.txt")
print_file_content("posts_from_JSONPlaceholder.txt")

print_stylish_separator("posts_headers_from_JSONPlaceholder.txt")
print_file_content("posts_headers_from_JSONPlaceholder.txt")

print_stylish_separator("post_request_to_JSONPlaceholder.txt")
print_file_content("post_request_to_JSONPlaceholder.txt")
