code
n, q = map(int, input().split())
signs = list(input())
sign_sum = 0
for sign in signs:
    if sign == '+':
        sign_sum += 1
    else:
        sign_sum -= 1

queries = []
for _ in range(q):
    l, r = map(int, input().split())
    left = right = l - 1
    window_sum = sign_sum
    removed = 0
    while left < r:
        if signs[left] == '+':
            window_sum -= 1
        else:
            window_sum += 1
        left += 1
    while right <= r:
        if signs[right] == '+':
            window_sum += 1
        else:
            window_sum -= 1
        right += 1
    queries.append(abs(window_sum - sign_sum))

print(*queries, sep='\n')
