#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(
        a, b, add(a, b), a, b, sub(a, b), a, b, mul(a, b), a, b, div(a, b)
    )

    print(result)
