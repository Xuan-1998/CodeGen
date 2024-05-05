import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        even_count = 0
        odd_count = 0
        for _ in range(n):
            num = int(sys.stdin.readline().strip())
            if num & (num - 1): # Check if the number is odd
                odd_count += 1
            else: # The number is even
                even_count += 1
        result = pow(2, k) ** even_count * (even_count + 1) % (10**9 + 7)
        print(result)

if __name__ == "__main__":
    solve()
