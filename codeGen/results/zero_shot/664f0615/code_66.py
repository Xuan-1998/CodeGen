v0, v1, t, delta = map(int, input().split())
speed_range = (min(v0, v1), max(v0, v1))
print(max((t-1)*delta+(t-v0)//(v1+v0//2)*(v1-v0)//(v1-v0) for v in range(*speed_range)))
