import sys

def solve():
    n = int(sys.stdin.readline())
    times = list(map(int, sys.stdin.readline().split()))
    healths = list(map(int, sys.stdin.readline().split()))

    times.sort()
    healths.sort()

    total_mana = 0
    i = j = 1
    while i <= len(times) and j <= len(healths):
        if times[i - 1] >= healths[j - 1]:
            total_mana += healths[j - 1]
            j += 1
        else:
            total_mana += times[i - 1] - (times[i - 1] % 2) + 1
            i += 1

    while i <= len(times):
        total_mana += times[i - 1] - (times[i - 1] % 2) + 1
        i += 1

    print(total_mana)

if __name__ == "__main__":
    solve()
