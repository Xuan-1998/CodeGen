from collections import defaultdict

def solve(n, k, requests):
    dp = [0] * (k + 1)
    request_map = defaultdict(list)

    for i, (ci, pi) in enumerate(requests):
        for j in range(min(i+1, k)+1):
            if ci <= j:
                dp[j] = max(dp[j], dp[j-ci]+pi*ci)
            else:
                dp[j] = max(dp[j], dp[j-1])
        request_map[dp[-1]].append((i, pi))

    total_earned = dp[-1]
    accepted_requests = []
    table_config = []

    for i in range(n):
        if dp[-1] == 0:
            break
        idx, _ = max(request_map[dp[-1]])
        accepted_requests.append(idx)
        total_earned -= requests[idx][1]
        table_config.append(requests[idx][0])
        dp[-1] -= requests[idx][0]

    print(f"{len(accepted_requests)} {total_earned}")
    for i, idx in enumerate(accepted_requests):
        print(f"{idx} {table_config[i]}")
