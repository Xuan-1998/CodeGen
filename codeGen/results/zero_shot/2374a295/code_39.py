k = int(input())
n = int(input())
mod = 1000000007
count = 0
i = 1
while i <= k:
    count += (1 << (k - i)) * pow(n, i, mod) % mod
    i += 1
print(count)
