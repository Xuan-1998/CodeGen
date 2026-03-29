n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_joy = sum(a) + sum(max(b), key=lambda x: a[b.index(x)])

print(total_joy)
