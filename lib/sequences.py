#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    if length == 0:
        print(fib_sequence)
        return fib_sequence
    else:
        fib_sequence.append(0)
        if length == 1:
            print(fib_sequence)
            return fib_sequence
        if length == 2:
            fib_sequence.append(1)
            print(fib_sequence)
            return fib_sequence
        for i in range(1,length -1 ):
            if fib_sequence[-1] == 0:
                fib_sequence.append(1)
                if length == 2:
                    print(fib_sequence)
                    return(fib_sequence)
            fib_sequence.append(fib_sequence[-1] + (fib_sequence[-2]))
        print(fib_sequence)
        return fib_sequence
