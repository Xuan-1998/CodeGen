import sys

def get_positive_invertible_matrices(n):
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            # Calculate the determinant and check if it's positive (or 1)
            determinant = i*j - j + i
            if determinant > 0:
                count += 1
    return count

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        print(get_positive_invertible_matrices(n))

if __name__ == "__main__":
    main()
