python
def smallest_string(n, k):
    s = input().strip()
    if k <= n:
        return s[:k]
    else:
        return (s + s)[:k]

n, k = map(int, input().split())
print(smallest_string(n, k))
