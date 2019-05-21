#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        my_division = 0
        try:
            my_division = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
            pass
        except(ValueError):
            pass
        except(TypeError):
            print("wrong type")
        except(ZeroDivisionError):
            print("division by 0")
        finally:
            new_list.append(my_division)
    return new_list
