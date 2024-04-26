# Read input
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

a_min = min(A)
b_min = min(B)

print(' '.join(map(str, A + [b_min]))), print(*sorted(B))
