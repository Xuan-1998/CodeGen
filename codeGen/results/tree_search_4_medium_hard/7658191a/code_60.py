def max_score(k, z, array):
    n = len(array)
    memo = {0: 0}

    for i in range(1, n+1):
        if i <= k:
            dp_i_right = memo.get(i-1, 0) + array[i-1]
            dp_i_left = max(memo.get(i-z-1, 0), 0) + array[i-1]
            dp_i = max(dp_i_right, dp_i_left)
        else:
            dp_i = memo.get(i-1, 0) + array[i-1]

        memo[i] = dp_i

    return memo[n-1]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    array = list(map(int, input().split()))
    print(max_score(k, z, array))
