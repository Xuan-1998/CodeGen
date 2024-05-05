def preprocess_array(signs):
    n = len(signs)
    cum_sum = [0] * (n + 1)
    for i in range(n):
        cum_sum[i + 1] = cum_sum[i] + (1 if signs[i] == "+" else -1)
    return cum_sum

def process_query(cum_sum, l, r):
    total_signs = cum_sum[r] - cum_sum[l - 1]
    if total_signs == 0:  # all signs are the same
        return 0  # no elements need to be removed

    min_remove = r - l + 1  # initially, we need to remove all elements
    for i in range(l, r):
        if cum_sum[i] * (r - i) <= total_signs:
            min_remove = i - l + 1  # found a better solution
            break

    return min_remove

def solve(input):
    n, q = map(int, input.split())
    signs = list(input.strip()[:-1])
    cum_sum = preprocess_array(signs)

    for _ in range(q):
        l, r = map(int, input().split())
        min_remove = process_query(cum_sum, l, r)
        print(min_remove)

# Example usage:
import sys
input = sys.stdin.readline
solve(input())
