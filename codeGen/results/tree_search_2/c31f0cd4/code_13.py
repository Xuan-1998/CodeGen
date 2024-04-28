N = int(input())
arr = list(map(int, input().split()))

print(' '.join(map(str, find_distinct_sums(N, arr))))
