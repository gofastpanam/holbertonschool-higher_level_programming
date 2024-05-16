#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if type(a) is int and type(b) is int:
            result = (a / b)
    except:
        return (None)
    finally:
        print("{}".format(result))
        return (result)
