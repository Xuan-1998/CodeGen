import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())

fraction = float(sys.stdin.readline().strip())

# apply rounding rules based on time limit t
rounding_index = 0
while t > 0 and rounding_index < n - 1:
    fraction *= 10
    fraction = round(fraction)
    t -= 1
    rounding_index += 1

print(int(fraction))
