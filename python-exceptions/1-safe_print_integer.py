#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print(end="")
        return (True)
    except (ValueError, TypeError, IndexError):
        return (False)
    finally:
        pass
