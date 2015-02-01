#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

import sys

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert i > 0
    assert j > 0
    assert i < 1000000
    assert j < 1000000

    loopIncrement = 1
    j+=1
    if(i > j):
        loopIncrement *= -1
        j-=2


    # print("Loop increment: " + str(loopIncrement))
    m = 1
    for x in range(i,j,loopIncrement):
        c = 1
        # print("running range. c: " + str(c) + " x: " + str(x) + " m: " + str(m) + " loop increment: " + str(loopIncrement))
        n = x
        while n > 1 :
            if (n % 2) == 0 :
                n = (n // 2)
            else :
                n = (3 * n) + 1
            c += 1
        assert c > 0
        m = max(c,m) 



    assert m > 0
    return m

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
