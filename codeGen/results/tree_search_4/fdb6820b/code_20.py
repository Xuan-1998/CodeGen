from functools import lru_cache

def count_ways(N, j):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    elif (N, j) in dp:  # base case: already computed
        return dp[(N, j)]
    else:
        total = 0
        for i in range(j):  # consider all array elements
            if arr[i] <= N:  # only include elements that can contribute to the sum
                total += count_ways(N - arr[i], j)  # recursive call with smaller N and same number of elements
        dp[(N, j)] = total
        return total

m, N = map(int, input().split())
arr = list(map(int, input().split()))
dp = {}  # initialize dictionary for memoization
@lru_cache(None)
def count_ways(N, j):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    elif (N, j) in dp:  # base case: already computed
        return dp[(N, j)]
    else:
        total = 0
        for i in range(j):  # consider all array elements
            if arr[i] <= N:  # only include elements that can contribute to the sum
                total += count_ways(N - arr[i], j)  # recursive call with smaller N and same number of elements
        dp[(N, j)] = total
        return total

print(count_ways(N, m) % (10**9 + 7))
