def solve(requests):
    k = int(input())  # number of tables
    dp = [0] * (len(requests) + 1)
    
    for i, (ci, pi) in enumerate(requests):
        for j in range(k+1):  # iterate over possible table sizes
            if ci <= j:
                dp[i+1] = max(dp[i], dp[i-1] + pi)
            else:
                break
    
    accepted_requests = [i for i in range(len(requests)) if requests[i][1] == dp[-1]]
    tables_needed = len(accepted_requests) // k + (len(accepted_requests) % k > 0)
    
    print(f"Accepted requests: {len(accepted_requests)}")
    print(f"Total amount of money earned: {dp[-1]}")
    for i, request in enumerate(accepted_requests):
        table = (i % k) + 1
        print(f"{request+1} {table}")

requests = []
for _ in range(int(input())):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

solve(requests)
