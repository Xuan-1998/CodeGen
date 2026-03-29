import sys

def max_grade():
    n, t = map(int, input().split())
    f = float(input())
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return True
        result = False
        for k in range(1, 11):  # assuming the maximum possible grade is 10.0
            if f < k / 10 ** i and t >= k:
                result = dp(i - 1, j - k)
                break
        memo[(i, j)] = result
        return result

    max_grade = 0
    for k in range(1, 11):  # assuming the maximum possible grade is 10.0
        if f < k / 10 ** n and t >= k:
            max_grade = k
            break
    while max_grade > 0 and not dp(n, t - int(max_grade * 10 ** n)):
        max_grade -= 1

    return str(int(max_grade))

print(max_grade())
