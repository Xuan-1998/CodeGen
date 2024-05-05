n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

k.sort()

required_mana = 0
for i in range(n):
    while h[i] > k[i]:
        required_mana += k[i] - (h[i] - 1) + 1
        h[i] -= (k[i] - (h[i] - 1) + 1)

print(required_mana)
