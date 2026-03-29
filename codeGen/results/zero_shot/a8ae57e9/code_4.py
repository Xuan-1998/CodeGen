import sys

n = int(input())
requests = []
for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

requests.sort(key=lambda x: x[0], reverse=True)

k = int(input())
table_capacity = [0] * k
for i in range(k):
    table_capacity[i] = int(input())

accepted_requests = 0
total_money_earned = 0
for ci, pi in requests:
    seated = False
    for i in range(k):
        if table_capacity[i] >= ci:
            table_capacity[i] -= ci
            total_money_earned += pi
            accepted_requests += 1
            print(f"{accepted_requests} {i+1}")
            seated = True
            break
    if not seated:
        print(f"Declined: {ci} people")

print(accepted_requests)
print(total_money_earned)
