import math

T = int(input())
for _ in range(T):
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        P, Ai, Bi = map(int, input().split())
        A.append(Ai)
        B.append(Bi)

    permutations = math.factorial(sum(set(A + B))) / (math.factorial(len(A)) * math.factorial(len(B)))
    probability = 1.0 / permutations
    print(probability)
