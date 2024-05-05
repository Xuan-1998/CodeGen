N = int(input())
M = int(input())
C = int(input())
U_1, U_2, ..., U_N = [int(x) for x in input().split()]
L_1, L_2, ..., L_M = [int(x) for x in input().split()]

result = count_x_sequences(N, M, C)
print(*result, sep=' ')
