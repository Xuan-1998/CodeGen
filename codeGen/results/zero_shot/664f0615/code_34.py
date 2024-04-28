v0, v1 = map(int, input().split())
t, delta = map(int, input().split())

if v0 <= 0 or v1 <= 0:
    print(0)
else:
    max_length = (v0 + v1) * t // (2 * delta) if delta > 0 else 0
    print(max_length)
