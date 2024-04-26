from itertools import combinations

MOD = 998244353

def f(S):
    T = []
    result = 0
    for op, x in S:
        if op == '+':
            T.append(x)
        elif op == '-' and T:
            T.remove(min(T))
    return sum(T)

def subseq_sum(A):
    total = 0
    for r in range(len(A) + 1):
        for subseq in combinations(A, r):
            total = (total + f(subseq)) % MOD
    return total

def main():
    n = int(input().strip())
    A = []
    for _ in range(n):
        op, *x = input().strip().split()
        x = int(x[0]) if x else None
        A.append((op, x))
    print(subseq_sum(A))

if __name__ == "__main__":
    main()
