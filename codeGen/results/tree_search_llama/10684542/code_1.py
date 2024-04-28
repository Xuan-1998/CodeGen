from collections import deque

def getExponent(n, p):
    queue = deque([(n, 0)])

    while queue:
        n, x = queue.popleft()
        if n % p == 0:
            return x
        if p <= 1:
            return None  # or raise an exception
        queue.append((n // p, x + 1))

# Example usage:
n, p = map(int, input().split())
print(getExponent(n, p))
