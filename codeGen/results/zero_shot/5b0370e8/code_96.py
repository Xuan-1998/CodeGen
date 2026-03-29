n, k = map(int, input().split())
count = 0
for _ in range(n):
    val = int(input())
    and_val = val & ((1 << k) - 1)
    xor_val = val ^ ((1 << k) - 1)
    if and_val >= xor_val:
        count += 1
print(count % (10**9 + 7))
