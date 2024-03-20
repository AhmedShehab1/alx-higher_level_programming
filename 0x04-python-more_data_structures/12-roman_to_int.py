#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    RomanDict = {'I':1, 'V':5, 'X':10, 'L':50,
    'C':100, 'D':500, 'M':1000}
    Result = 0
    for j in range(len(roman_string)):
        eqv_Value = RomanDict[roman_string[j]]
        if j != len(roman_string) - 1:
            if eqv_Value < RomanDict[roman_string[j + 1]]:
                Result -= eqv_Value
            else:
                Result += eqv_Value
        else:
            Result += eqv_Value
    return Result
