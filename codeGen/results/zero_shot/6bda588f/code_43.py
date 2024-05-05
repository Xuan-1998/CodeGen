# Define the input function
def input():
    return map(int, raw_input().split())

n, s = input()

a = input()

f = 0

for i in range(n):
    f += (a[i]-s) * (2*s-a[i])

print min(f)
