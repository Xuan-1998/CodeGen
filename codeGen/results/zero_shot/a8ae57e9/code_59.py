code
import sys

def solve():
    n = int(sys.stdin.readline())
    requests = []
    for _ in range(n):
        group_size, total_amount = map(int, sys.stdin.readline().split())
        requests.append((group_size, total_amount))

    k = int(sys.stdin.readline())
    max_capacity = int(sys.stdin.readline())

    requests.sort(key=lambda x: x[1] / x[0], reverse=True)

    accepted_requests = 0
    total_earned = 0
    table_assignments = []

    for group_size, total_amount in requests:
        for i in range(k):
            if max_capacity - (i + 1) >= group_size:
                table_assignments.append((accepted_requests, i))
                accepted_requests += 1
                total_earned += total_amount
                break

    print(accepted_requests, total_earned)
    for assignment in table_assignments:
        print(*assignment)

if __name__ == "__main__":
    solve()
code
