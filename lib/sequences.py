#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    
    fib = [0,1]

    while len(fib) < n:
        fib.append(fib[-2] + fib[-1])
    print(fib)


print_fibonacci(9)