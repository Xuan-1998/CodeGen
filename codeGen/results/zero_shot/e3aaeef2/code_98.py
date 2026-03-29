def getLength(n, m):
    # Calculate the maximum possible length that the number could have
    max_length = len(str(n))
    for _ in range(m):
        n += 1
        max_length = max(max_length, len(str(n)))

    # Calculate the actual length of the resulting number modulo 10^9+7
    actual_length = (max_length + m) % ((10**9 + 7))

    return actual_length

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(getLength(n, m))
