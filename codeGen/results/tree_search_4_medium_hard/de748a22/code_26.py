def query(arr, l, r):
    prefix_sum = 0
    for i in range(l-1, r):
        if arr[i] == "+":
            prefix_sum += 1
        else:
            prefix_sum -= 1

    if prefix_sum == 0:
        return 0
    elif prefix_sum > 0:
        return r - l + 1
    else:
        return r - l


n, q = map(int, input().split())
arr = list(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(query(arr, l, r))
