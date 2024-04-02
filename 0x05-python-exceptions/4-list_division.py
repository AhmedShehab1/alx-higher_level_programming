#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        x = 0
        new_list = []
        while (x < list_length + 1):
                try:
                        new_list.append(my_list_1[x] / my_list_2[x])
                except TypeError:
                        new_list.append(0)
                        print("wrong type")
                except ZeroDivisionError:
                        new_list.append(0)
                        print("division by zero")
                except IndexError:
                        new_list.append(0)
                        print("out of range")
                finally:
                        x += 1
                        if x == list_length:
                                return new_list
                