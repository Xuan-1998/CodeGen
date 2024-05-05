n, x = map(int, input().split())
a = list(map(int, input().split()))
prefix_xor = [0]
for i in range(n):
    prefix_xor.append(prefix_xor[i] ^ a[i])
max_sum = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        xor_value = prefix_xor[j] - prefix_xor[i-1]
        max_sum = max(max_sum, xor_value + x if a[i-1] < a[j-1] else xor_value)
print(max_sum)
