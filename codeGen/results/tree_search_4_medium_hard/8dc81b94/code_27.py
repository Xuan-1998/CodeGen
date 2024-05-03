def make_zero():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = {(0, k): (k == 0) for k in range(2)}

    for i in range(1, n):
        for k in range(2):
            dp[(i, k)] = (dp.get((i-1, k-(arr[i]-1)%2), False) and arr[i] > 0) or \
                         (dp.get((i-1, k+(arr[i]-1)%2), False))

    for k in range(2):
        if dp[(n-1, k)]:
            return "YES"
    return "NO"

print(make_zero())
