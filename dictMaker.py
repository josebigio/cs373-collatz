#!/usr/bin/env python3

cycleLengthCache = dict()

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
        print( str(x) + ":" + str(c) + ",", end = "" )
        m = max(c,m) 

    assert m > 0
    return m

def main():
    collatz_eval(1,5000)

if __name__ == '__main__':
    main()