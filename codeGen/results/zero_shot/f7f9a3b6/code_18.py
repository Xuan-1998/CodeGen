n = int(input())
s = input()
a = [int(x) for x in input().split()]

ways, max_len, min_substrs = solve(s, a, n)

print(ways)
print(max_len)
print(min_substrs)
