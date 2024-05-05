n, k = map(int, input().split())
s = input()

ans = s

if len(s) < k:
    ans *= (k // len(s)) + 1

print(ans[:k])
