#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            division_result = 0
            if (isinstance(my_list_1[i], (int, float))
                    and isinstance(my_list_2[i], (int, float))):
                if my_list_2[i] != 0:
                    division_result = my_list_1[i] / my_list_2[i]
                else:
                    raise ZeroDivisionError
            else:
                raise TypeError("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except (IndexError, TypeError):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            else:
                print("wrong type")
        finally:
            result.append(division_result)
    return result


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
