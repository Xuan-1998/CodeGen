def min_changes(s, k):
    n = len(s)
    good_substrings = 0
    for i in range(n - k + 1):
        if s[i:i+k] == 'RGBRGBRGB...'[:k]:
            good_substrings += 1
    return n - good_substrings * k

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
