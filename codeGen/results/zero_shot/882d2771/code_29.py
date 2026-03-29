t, l, r = map(int, input().split())
f_values = [0] * (r + 1)
for i in range(2, r + 1):
    f_values[i] = i - 1

print(((t * sum(f_values[l:r+1])) % (10**9 + 7)) - ((l * f_values[r]) % (10**9 + 7))))
