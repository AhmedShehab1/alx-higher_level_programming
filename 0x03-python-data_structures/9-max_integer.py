def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return "None"
    else:
        Max = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > Max:
                Max = my_list[i]
        return Max
