def solve(N, K, Arr):
    memo = {(0, 0): 1}  # base case: empty subarray
    count = 0

    for i in range(1, N):
        max_val = max(Arr[i], memo[(i-1, max(Arr[:i+1]))][1])
        if max_val > K:
            count += memo.get((i-1, max_val), 0)

        memo[(i, max_val)] = count + (max_val > K)

    return memo[N-1][1]

N = int(input())
K = int(input())
Arr = [int(x) for x in input().split()]
print(solve(N, K, Arr))
