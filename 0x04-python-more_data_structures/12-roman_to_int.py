#!/usr/bin/python3


# roman_to_int - converts a roman numeral to an integer.
def roman_to_int(roman_string):
    if roman_string:
        num = 0
        if roman_string is "IV":
            return 4
        elif roman_string is "IX":
            return 9
        elif roman_string is "XL":
            return 40
        elif roman_string is "XC":
            return 90
        elif roman_string is "CD":
            return 400
        elif roman_string is "CM":
            return 900
        else:
            for i in roman_string:
                if i == 'M':
                    num += 1000
                elif i == 'D':
                    num += 500
                elif i == 'C':
                    num += 100
                elif i == 'L':
                    num += 50
                elif i == 'X':
                    num += 10
                elif i == 'V':
                    num += 5
                elif i == 'I':
                    num += 1
                else:
                    return 0
            return num
    else:
        return 0
