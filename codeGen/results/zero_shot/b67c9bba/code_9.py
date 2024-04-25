from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(lst):
    return reduce(lcm, lst)

def expected_shuffles(n):
    # Since each permutation of the n-1 elements (excluding the already sorted one) has equal probability,
    # the expected number of shuffles is the same as the average number of shuffles for all (n-1)! permutations.
    # This is equivalent to the least common multiple (LCM) of the cycle lengths in the permutation group of n-1 elements.
    cycle_lengths = [i for i in range(2, n+1)]
    return lcm_of_list(cycle_lengths)

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = expected_shuffles(n)
        print(f"{result}/1")  # Since the result is LCM, it's always an integer, so the fraction is result/1.

if __name__ == "__main__":
    main()
