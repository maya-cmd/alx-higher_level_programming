#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    output = []
    for i in range(list_length):
        try:
            div_output = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            div_output = 0

        except (TypeError, ValueError):
            print("wrong type")
            div_output = 0

        except IndexError:
            print("out of range")
            div_output = 0

        finally:
            output.append(div_output)
    return output
