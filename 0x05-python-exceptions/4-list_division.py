#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    for idx in range(0, list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except ValueError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list[idx] = result
    return new_list
