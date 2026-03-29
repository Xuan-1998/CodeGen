import sys

def read_input():
    t = int(input())
    dp = [0] * (n+1)
    for _ in range(t):
        n = int(input())
        parent = list(map(int, input().split()))
        l = list(map(int, (input() for _ in range(n)).split()))
        r = list(map(int, (input() for _ in range(n)).split()))
        # Implement your logic here to adjust the values and store the minimum number of operations.
    return dp

def main():
    dp = read_input()
    print(*dp)

if __name__ == "__main__":
    main()
