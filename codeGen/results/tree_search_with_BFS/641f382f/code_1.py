import math
from sys import stdin

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if 1 in a:
        print(n - a.count(1))
        return
    min_dist = n + 1
    for i in range(n):
        gcd = a[i]
        j = i
        while j < n and j - i + 1 < min_dist:
            gcd = math.gcd(gcd, a[j])
            if gcd == 1:
                min_dist = j - i + 1
                break
            j += 1
    if min_dist == n + 1:
        print(-1)
    else:
        print(min_dist + n - 2)

if __name__ == "__main__":
    main()

