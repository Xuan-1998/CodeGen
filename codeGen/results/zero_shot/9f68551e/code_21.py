import sys

def find_least_mana():
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))

    k_h = list(zip(k, h))
    k_h.sort()

    for i in range(n):
        prev_damage = 0 if i == 0 else k_h[i-1][0] + 1
        current_mana = prev_damage - (k_h[i][1] - 1) if k_h[i][1] > 1 else 0

        least_mana = min(least_mana, current_mana)

    return int(least_mana)

if __name__ == '__main__':
    sys.stdin.readline()  # Discard first line
    t = int(sys.stdin.readline())
    for _ in range(t):
        print(find_least_mana())
