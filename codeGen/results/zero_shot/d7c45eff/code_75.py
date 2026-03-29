n, k = map(int, input().split())
s = input()

if k <= n:
    if s[:k] < s[:k-1]:
        print(s[:k])
    else:
        duplicated_s = s + s
        if duplicated_s[:k] < s[:k]:
            print(duplicated_s[:k])
        else:
            print(s)
else:
    print(s)
