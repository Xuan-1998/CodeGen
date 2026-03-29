def count_ways(n_upper, m_lower):
    mod = 10**9 + 7

    # Base case when there are no more hemispheres of any kind
    if n_upper == 0 or m_lower == 0:
        return 1 if min(n_upper, m_lower) < C else 0

    # Initialize the memo dictionary
    memo = {(set(), set()): 1}

    for _ in range(n_upper + m_lower):
        new_dp = {}
        for (upper, lower) in list(memo.keys()):
            for u in upper:
                if all(l > u for l in lower):
                    new_dp[lower | {u}] = (new_dp.get(upper - {u}, 0) or 0) + memo[(upper, lower)]
            for l in lower:
                if all(u < l for u in upper):
                    new_dp[upper | {l}] = (new_dp.get((set(), set()) | {(lower - {l})}, 0) or 0) + memo[(upper, lower)]
        memo.update(new_dp)

    return memo[(set(), set())] % mod

C = int(input())
T = int(input())

for _ in range(T):
    N, M, _ = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    
    print(count_ways(len(U), len(L)))
