s0, s1 = map(int, input().split())
t, d = map(int, input().split())

print((min(s0, s1) + max(0, abs(s1 - s0))) * t)
