# Read input
t, l, r = map(int, input().split())

# Initialize variables
f_sum = 0

for i in range(l, r+1):
    f_sum += (i-l)*math.comb(i, (i-l)//2)

print((sum([t*math.comb(i, (i-l)//2) for i in range(l, r+1)]) - l*math.comb(r, (r-l)//2)) % (10**9 + 7))
