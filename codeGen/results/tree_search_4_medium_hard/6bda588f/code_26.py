code block for memoization:
dp = {}
def min_func(a, s):
    if len(a) == 1:
        return a[0]
    if (a, s) in dp:
        return dp[(a, s)]
    result = float('inf')
    for i in range(len(a)):
        x = y = a[i] // 2
        while x * (a[i] - 2*x) >= s*s and x <= a[i]:
            temp = min_func(a[:i]+[x], s)
            if temp < result:
                result = temp
            x -= 1
    dp[(a, s)] = result
    return result

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(min_func(a, s))
