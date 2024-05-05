n = int(input())  # number of booking requests
k = int(input())  # number of tables available
requests = []

for _ in range(n):
    ci, pi = map(int, input().split())
    requests.append((ci, pi))

# TO DO: Implement the logic to determine which requests to accept and decline
