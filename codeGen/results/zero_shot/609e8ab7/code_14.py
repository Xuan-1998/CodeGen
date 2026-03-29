    return ans

n = int(input())
p = [int(x) for x in input().split()]
l = [int(x) for x in (input() for _ in range(n))]
r = [int(x) for x in (input() for _ in range(n))]

print(min_operations(n, p, l, r))
