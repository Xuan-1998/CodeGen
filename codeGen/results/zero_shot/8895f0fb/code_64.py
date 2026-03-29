import sys

def expected_non_zero_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        carries_sum = 0
        total_pairs = N * (N + 1) // 2
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                carry_count = 0
                a, b = str(i), str(j)
                while len(a) < N or len(b) < N:
                    a = '0' + a
                    b = '0' + b
                for k in range(N):
                    if int(a[k]) + int(b[k]) >= 10:
                        carry_count += 1
                carries_sum += carry_count
        print(carries_sum / total_pairs)

if __name__ == "__main__":
    expected_non_zero_carries()
