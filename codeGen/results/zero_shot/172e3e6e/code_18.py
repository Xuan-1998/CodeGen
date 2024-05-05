import sys

def count_good_subsequences():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    good_count = 0
    for i in range(1, n+1):
        subsequence = [a[j] for j in range(i-1, -1, -1) if (i-1-j) % i == 0]
        if all(k % i == 0 for k in subsequence):
            good_count += 1

    print(good_count % (10**9 + 7))

count_good_subsequences()
