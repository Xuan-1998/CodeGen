import sys

n = int(sys.stdin.readline())
requests = []

for i in range(n):
    ci, pi = map(int, sys.stdin.readline().split())
    requests.append((ci, pi))

requests.sort(key=lambda x: x[1], reverse=True)

accepted_requests = 0
total_earned = 0
available_capacity = k * max_capacity

for ci, pi in requests:
    if available_capacity >= ci:  # check if table has enough capacity
        accepted_requests += 1
        total_earned += pi
        available_capacity -= ci

print(accepted_requests, total_earned)
