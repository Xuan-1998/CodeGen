import sys

def solve():
    n = int(sys.stdin.readline())
    ci_pi = [list(map(int, line.split())) for _ in range(n)]
    ci_pi.sort(key=lambda x: x[1], reverse=True)
    k = int(sys.stdin.readline())
    ri = [int(sys.stdin.readline()) for _ in range(k)]

    accepted_requests = 0
    total_earned = 0
    table_assignments = []

    for group_size, money in ci_pi:
        for i in range(k):
            if ri[i] >= group_size:
                ri[i] -= group_size
                total_earned += money
                accepted_requests += 1
                table_assignments.append((accepted_requests, i+1))
                break

    print(accepted_requests)
    print(total_earned)
    for assignment in table_assignments:
        print(*assignment)

if __name__ == "__main__":
    solve()
