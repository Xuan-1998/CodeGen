def can_make_zero(arr):
    n = len(arr)
    memo = {}

    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == j:
            return 'NO' if arr[i] > 0 else 'YES'
        
        if i >= n or j < 0:
            return 'NO'
        
        if arr[i] > 0 and arr[j] > 0:
            return 'NO'
        
        if arr[i] <= 0 and arr[j] <= 0:
            result = f(i + 1, j)
            if result == 'YES':
                return 'YES'
            else:
                return result
        
        if arr[i] > 0:
            result = f(i + 1, j)
            if result == 'YES':
                return 'YES'
            else:
                return result
        elif arr[j] > 0:
            result = f(i, j - 1)
            if result == 'YES':
                return 'YES'
            else:
                return result
        
        memo[(i, j)] = 'YES' if (arr[i] <= 0 and f(i + 1, j) == 'YES') or (arr[j] <= 0 and f(i, j - 1) == 'YES') else 'NO'
        return memo[(i, j)]

    arr.sort()
    result = 'YES'
    for i in range(n):
        if arr[i] > 0:
            result = f(0, i)
            break
    for i in range(n - 1, -1, -1):
        if arr[i] > 0:
            result = f(i, n - 1)
            break
    return 'YES' if result == 'YES' else 'NO'
