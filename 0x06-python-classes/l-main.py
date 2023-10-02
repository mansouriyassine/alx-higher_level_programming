#!/usr/bin/python3

if __name__ == "__main__":
    mc1 = MagicClass(5)
    print("Radius:", mc1.__radius)
    print("Area:", mc1.area())
    print("Circumference:", mc1.circumference())

    try:
        mc2 = MagicClass("not_a_number")
    except TypeError as e:
        print("Error:", e)
