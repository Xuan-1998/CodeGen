import sys

T = int(sys.stdin.readline())
probs_list = []
for _ in range(T):
    n = int(sys.stdin.readline())
    probs = []
    for i in range(n):
        P, A, B = map(float, sys.stdin.readline().split())
        probs.append((P, A, B))
    probs_list.append(probs)

for probs in probs_list:
    prob = 1
    for P, A, B in probs:
        prob *= (P / 100) ** (A != B)
    print("{:.6f}".format(prob))
