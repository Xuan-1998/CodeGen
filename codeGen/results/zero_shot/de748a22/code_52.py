code
n, q = map(int, input().split())
signs = list(input())
total_sum = sum(map(lambda x: 1 if x == "+" else -1, signs))

for _ in range(q):
    l, r = map(int, input().split())
    subarray_sum = sum(map(lambda x: 1 if x == "+" else -1, signs[l-1:r]))
    min_removals = abs(subarray_sum - total_sum)
    print(min_removals)
