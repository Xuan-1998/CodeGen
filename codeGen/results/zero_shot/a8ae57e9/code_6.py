from sys import stdin

def solve():
    n, k = map(int, stdin.readline().split())
    requests = [list(map(int, stdin.readline().split())) for _ in range(n)]
    requests.sort(key=lambda x: x[0], reverse=True)
    table_assignments = []
    accepted_requests = 0
    total_earned_money = 0

    for i, request in enumerate(requests):
        group_size, money = request
        for j in range(k):
            if sum(1 for _ in range(k)) - (j+1) >= group_size:
                table_assignments.append((i+1, j+1))
                accepted_requests += 1
                total_earned_money += money
                break

    print(accepted_requests, total_earned_money)
    for assignment in table_assignments:
        print(*assignment)

solve()
