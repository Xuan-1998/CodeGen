import numpy as np
from scipy.integrate import odeint
import sys

def bouncing_ball(y, t):
    x, v = y
    dxdt = v
    dvdt = -np.sign(v) / k
    return [dxdt, dvdt]

k = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
x0 = int(sys.stdin.readline().strip())

y0 = [0, 1]  # initial condition: ball at the starting end, moving forward

t = np.linspace(0, k * (2*n + 1), 10000)

solution = odeint(bouncing_ball, y0, t)
x = solution[:, 0]

print("YES" if x.min() < x0 else "NO")
