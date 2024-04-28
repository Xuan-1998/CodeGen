v0, v1, t, delta = map(int, input().split())
length = 0
speed = v0
for _ in range(t):
    length += speed
    if _ == t - 2:
        break
    speed += min(delta, v1 - v0)
print(length)
