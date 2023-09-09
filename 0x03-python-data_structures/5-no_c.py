#!/usr/bin/python3
def no_c(my_string):
    result = ""

    for char in my_string:
        # Check if the character is not 'c' or 'C' and add it to the result
        if char != 'c' and char != 'C':
            result += char


return result

if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
