#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tup_a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    tup_a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    tup_b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    tup_b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (tup_a1 + tup_b1, tup_a2 + tup_b2)
