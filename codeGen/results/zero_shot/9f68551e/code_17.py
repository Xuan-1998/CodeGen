import sys

def main():
    n = int(sys.stdin.readline())
    k_i = list(map(int, sys.stdin.readline().split()))
    k_i.sort()
    h_i = list(map(int, sys.stdin.readline().split()))

    min_mana_required = 0
    for i in range(n):
        while k_i[i] > min_mana_required + 1:
            min_mana_required += 1

    print(min_mana_required)

if __name__ == "__main__":
    main()
