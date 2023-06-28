#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    other_list = []

    for k in range(list_length):
        try:
            other_list.append(my_list_1[k] / my_list_2[k])
        except ZeroDivisionError:
            other_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            other_list.append(0)
            print("out of range")
            continue
        except TypeError:
            other_list.append(0)
            print("Wrong type")
            continue
        finally:
            pass
    return other_list
