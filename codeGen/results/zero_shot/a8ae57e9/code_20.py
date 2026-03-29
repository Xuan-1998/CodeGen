import sys

def solve():
    n = int(input())
    requests = []
    for _ in range(n):
        ci, pi = map(int, input().split())
        requests.append((ci, pi))

    requests.sort(key=lambda x: x[1], reverse=True)

    k, r = map(int, input().split())
    available_tables = [r] * k
    total_earned = 0
    n_accepted = 0

    for ci, pi in requests:
        for i in range(k):
            if available_tables[i] >= ci:
                available_tables[i] -= ci
                total_earned += pi
                print(f"{n_accepted + 1} {i + 1}")
                n_accepted += 1
                break

    print(n_accepted)
    print(total_earned)

if __name__ == "__main__":
    solve()
