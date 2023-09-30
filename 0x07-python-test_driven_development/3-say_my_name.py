#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the full name.
    """
    error1 = "first_name must be a string"
    error2 = "last_name must be a string"

    if type(first_name) is not str:
        raise TypeError(error1)

    if type(last_name) is not str:
        raise TypeError(error2)

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")

    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
