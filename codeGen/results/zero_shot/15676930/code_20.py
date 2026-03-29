n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

max_joy = max_joy(n, a, b, c)
print(max_joy)
