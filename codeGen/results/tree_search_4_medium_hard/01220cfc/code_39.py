def canJump(arr):
    memo = [False] * len(arr)
    memo[0] = True

    for i in range(1, len(arr)):
        if not memo[i]:
            continue

        j = max((j := i - arr[i]) for j in range(i) if j >= 0 and memo[j])
        if j < len(arr) - 1:
            memo[i] = True
        else:
            memo[i] = memo[-1]

    return memo[-1]
