def max_beauty(a):
    max_b = 0
    for s in a:
        b = f(s)
        if b > max_b:
            max_b = b
    return max_b

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_beauty(a))
