from collections import defaultdict
from sys import stdin

def read_query():
    return [int(x) for x in input().split()]

def calculate_min_removals(signs, l, r):
    total_signs = 0
    sign_sum = 0
    min_removals = float('inf')

    for i in range(l-1, r):
        total_signs += 1
        sign_sum += signs[i]
        if sign_sum == 0:
            return 0

        if i >= l-1 and (i-r+1)%2==1:
            min_removals = min(min_removals, total_signs)
        
    return min_removals

def main():
    read_query()  # Read n and q
    n = int(input())
    signs = list(input())

    for _ in range(int(read_query()[0])):
        l, r = map(int, input().split())
        print(calculate_min_removals(signs, l, r))

if __name__ == "__main__":
    main()
