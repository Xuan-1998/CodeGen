from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    requests = []

    for _ in range(n):
        gi, pi = map(int, input().split())
        requests.append((gi, pi))

    requests.sort(reverse=True)  # Sort by group size

    for gi, pi in requests:
        while k - gi < 0:  # Not enough tables
            break
        dp[k-gi] += pi
        k -= gi

    print(f"{dp[0]} {len([request for request in requests if request[1] <= dp[0]])}")
