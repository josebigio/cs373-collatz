#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# global_varz
# ------------
cycleLengthCache = dict()


# ------------
# collatz_read
# ------------

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

    start = i
    end = j
    if(i>j):
        start = j
        end = i


    t = (end>>1)+1
    if(t>start):
        start = t
    
   
    m = 1
    for x in range(start,end+1):
        c = 1
        if(x in cycleLengthCache):
            c = cycleLengthCache[x]
        else:
            n = x
            while n > 1 :
                if(n in cycleLengthCache):
                    c+=cycleLengthCache[n]-1
                    break
                else:
                    if (n % 2) == 0 :
                        n = (n // 2)
                        c +=1
                    else :
                        n = n + (n>>1) + 1
                        c += 2
            assert c > 0
        cycleLengthCache[x] = c
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
