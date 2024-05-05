import sys

def solve():
    n = int(input())
    uvs = [list(map(int, input().split())) for _ in range(n - 1)]
    m = int(input())
    primes = list(map(int, input().split()))

    # Your implementation goes here...

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    solve()
