import sys

v0, vf, t, dv = map(int, (line.split() for line in sys.stdin).next().split())
speeds = [v0 + i*dv for i in range(t)]
print(max(sum(1 if v <= speed < v+dv for v in range(v0, vf+1)) for speed in speeds))
