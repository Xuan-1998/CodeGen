import sys

def read_input():
    T = int(sys.stdin.readline().strip())
    matrix_count = 0
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        # Code will go here
        pass
    return T, matrix_count

def main():
    T, matrix_count = read_input()
    print(matrix_count)

if __name__ == "__main__":
    main()
