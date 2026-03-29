import sys

n, k = map(int, input().split())
requests = []
for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_money_earned = 0

tables = [0] * k

for ci, pi in requests:
    for i in range(k):
        if tables[i] + ci <= k: 
            tables[i] += ci
            accepted_requests += 1
            total_money_earned += pi
            print(f"{accepted_requests} {i+1}")
            break

print(f"{accepted_requests} {total_money_earned}")
