n, k = map(int, input().split())
s = input()

if k >= n:
    print(s)

original = s
duplicated = s * 2

if s <= duplicated:
    print(original)
else:
    print(duplicated)
