def min_function(a):
    return sum((ai//2) * (2*s + ai - 2*s) for ai in a)

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_function(a))
