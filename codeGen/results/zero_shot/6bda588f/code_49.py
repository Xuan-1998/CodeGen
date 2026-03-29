def min_value(n, s, a):
    return s * sum(a)

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_value(n, s, a))
