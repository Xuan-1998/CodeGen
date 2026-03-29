def merge_ways(M):
    n = len(M)
    ways = 0
    for m_i in M:
        unique_elements = set(range(1, n+1)) - set([m_i])
        ways += len(unique_elements) % (10**9 + 7)
    return ways

n = int(input())
M = [int(x) for x in input().split()]
print(merge_ways(M))
