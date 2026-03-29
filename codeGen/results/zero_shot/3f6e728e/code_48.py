code
N = int(input())
M = int(input())
C = int(input())
upper_radii = list(map(int, input().split()))
lower_radii = list(map(int, input().split()))

total_permutations = 1
for radius in sorted(upper_radii + lower_radii):
    total_permutations *= (2 ** (C - radius))

print(total_permutations % (10**9 + 7))
