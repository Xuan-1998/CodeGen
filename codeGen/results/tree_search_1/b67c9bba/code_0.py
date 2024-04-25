from math import factorial
from fractions import Fraction

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def solve(n):
    dp_table = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i):
            sum_expected_shuffles = Fraction(0)
            total_ways_to_shuffle = factorial(i - j)
            for k in range(i - j + 1):
                ways_to_place_k_correctly = nCr(i - j, k) * factorial(k)
                if k != i - j:
                    sum_expected_shuffles += ways_to_place_k_correctly * (dp_table[i][j + k] + 1)
            dp_table[i][j] = sum_expected_shuffles / (total_ways_to_shuffle - ways_to_place_k_correctly)
    return dp_table[n][0]

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = solve(n)
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()
