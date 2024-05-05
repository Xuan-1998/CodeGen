python
while True:
    s = input().strip()
    n, k = map(int, input().split())
    if n == 0:
        break

    if len(s) <= k:
        print(s)
    else:
        if s[0] < s[-1]:
            print(s[:k])
        else:
            print(s[:k//2] + s[k//2:])
