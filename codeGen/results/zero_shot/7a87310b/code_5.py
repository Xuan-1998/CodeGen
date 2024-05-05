import sys

def count_matrices():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        count = 0
        for i in range(3, 25001):
            for j in range(i+1, 25001):
                if (i + j) == N and abs(i*j - (j-i)) > 0:
                    count += 1
        print(count)

count_matrices()
