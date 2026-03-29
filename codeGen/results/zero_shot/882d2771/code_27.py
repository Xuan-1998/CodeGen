import sys

def solve():
    t, l, r = map(int, input().split())
    f = lambda n: int((n * (n - 1) / 2).bit_length())  # approximate f(n)
    
    total_sum = 0
    for i in range(t):
        total_sum += ((l + i) ** 2) % (10**9 + 7) * f(l + i)
    total_sum -= l * f(r)

    print(total_sum % (10**9 + 7))

if __name__ == "__main__":
    solve()
