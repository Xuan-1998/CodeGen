def min_marks_below_water(n, marks):
    memo = {0: 0}
    for i in range(1, n+1):
        if i-1 not in memo:
            memo[i] = min(marks[i-1], memo.get(i-1, float('inf')))
        else:
            memo[i] = min(marks[i-1] + memo[i-1], memo[i-1])
    return memo[n]

n = int(input())
marks = list(map(int, input().split()))
print(min_marks_below_water(n, marks))
