import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probs = []
        for _ in range(n):
            P, A, B = map(float, sys.stdin.readline().split())
            prob_A = P / 100
            prob_B = 1 - prob_A
            if A == B:
                prob_same = prob_A * prob_A + (1 - prob_A) * (1 - prob_A)
                prob_correct = prob_A * prob_B * (1 - prob_same)
            else:
                prob_correct = prob_A * prob_B
            probs.append(prob_correct)
        print(sum(probs))

if __name__ == "__main__":
    solve()
