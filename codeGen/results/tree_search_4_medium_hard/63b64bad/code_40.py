def f(i, x, y):
    if x <= 0 or x > n:
        return y
    x += a[x]
    y += a[x]
    x -= a[x]
    y += a[x]
    return (i+1, x, y)

def g(i):
    current_state = (i-1, 1, 0)
    while True:
        current_state = f(*current_state)
        if current_state[1] <= 0 or current_state[1] > n:
            break
    return current_state[2]

n = int(input())
a = list(map(int, input().split()))
dp = {1: -1}
for i in range(2, n+1):
    dp[i] = g(i)
print('\n'.join(str(y) for y in dp.values()))
