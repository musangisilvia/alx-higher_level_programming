#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    if lenA >= 2 and lenB >= 2:
        res = tuple(map(lambda i, j: i + j, tuple_a[0:2], tuple_b[0:2]))
        return res
    elif lenB < 2 and lenB != 0:
       lsb = list(tuple_b)
       lsb.append(0)
       tb = tuple(lsb)
       res1 = tuple(map(lambda i, j: i + j, tuple_a[0:2], tb[0:2]))
       return res1
    elif lenB == 0:
        ls = list(tuple_b)
        ls.append(0)
        ls.append(0)
        tp = tuple(ls)
        res = tuple(map(lambda i, j: i + j, tuple_a[0:2], tp[0:2]))
        return res
