import sys
from math import prod

def find_prime_factors(k):
    prime_factors = []
    i = 2
    while k > 1:
        if k % i == 0:
            prime_factors.append(i)
            k //= i
        else:
            i += 1
    return prime_factors

def max_distribution_index(n, edges, k):
    result = 0
    for u, v in edges:
        # Calculate the sum of numbers on the simple path from node u to node v
        sum_path = ...  # implement this step
        if prod(sum_path) == k:
            result += sum_path
    return result

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = [list(map(int, input().split())) for _ in range(n-1)]
        m = int(input())
        prime_factors = find_prime_factors(k)
        # implement the recursive function or dynamic programming here
        result = max_distribution_index(n, edges, k)
        print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
