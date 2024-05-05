def smallest_string(n, k):
    if k == n:
        return s
    elif k > n:
        return smallest_string(n, k-1)
    else:
        return min(s[:-1], s+s)[min(range(n), key=lambda i: (s[i], i))[:k]]

n, k = map(int, input().split())
s = input()
print(smallest_string(n, k))
