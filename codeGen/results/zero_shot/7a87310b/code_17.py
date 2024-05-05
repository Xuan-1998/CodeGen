import sys

def count_matrices():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        count = 0
        for i in range(-N//2, (N+1)//2 + 1):
            for j in range(-N//2, (N+1)//2 + 1):
                if abs(i) + abs(j) == N and i * j > 0:
                    count += 1
        print(count)

if __name__ == "__main__":
    count_matrices()
