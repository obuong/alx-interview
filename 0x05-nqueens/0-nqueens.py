#!/usr/bin/python3
""" N queens """
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    exit(1)

def print_n_must_be_number_and_exit():
    print("N must be a number")
    exit(1)

def print_n_must_be_at_least_4_and_exit():
    print("N must be at least 4")
    exit(1)

def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(n):
    """ solve """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    if not sys.argv[1].isdigit():
        print_n_must_be_number_and_exit()

    n = int(sys.argv[1])

    if n < 4:
        print_n_must_be_at_least_4_and_exit()

    solve(n)
