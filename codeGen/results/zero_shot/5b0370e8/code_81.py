import sys
from collections import defaultdict

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().strip().split())
        count_and_ge_xor = 0
        and_counts = [defaultdict(int) for _ in range(k+1)]
        xor_counts = [defaultdict(int) for _ in range(k+1)]

        for num in map(int, sys.stdin.readline().strip().split()):
            for i in range(k+1):
                if (num & (1 << i)) > 0:
                    and_counts[i][1] += 1
                else:
                    and_counts[i][0] += 1

            for i in range(k+1):
                xor_counts[i][(num >> i) & 1] += 1

        for mask in range(2**k):
            and_val = sum(1 << i for i in range(k) if and_counts[i][1])
            xor_val = sum((mask >> i) & 1 for i in range(k))
            if and_val >= xor_val:
                count_and_ge_xor += 1

        print(count_and_ge_xor % (10**9 + 7))

if __name__ == "__main__":
    main()
