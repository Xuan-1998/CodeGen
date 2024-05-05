import sys

def read_input():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        k_i = list(map(int, sys.stdin.readline().strip().split()))
        h_i = list(map(int, sys.stdin.readline().strip().split()))
        yield n, k_i, h_i

def total_mana(n, k_i, h_i):
    total_mana = 0
    current_health = 1
    for i in range(1, n + 1):
        while k_i[i - 1] > k_i[i - 2]:
            if current_health <= h_i[i - 1]:
                return -1
            current_health += 1
        total_mana += current_health
    return total_mana

if __name__ == "__main__":
    for n, k_i, h_i in read_input():
        print(total_mana(n, k_i, h_i))
