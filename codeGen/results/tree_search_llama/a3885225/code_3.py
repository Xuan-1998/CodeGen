import sys

def solve():
    T = int(input())  # number of test cases
    for _ in range(T):
        N = int(input())  # length of binary string
        S = input()  # binary string
        zero_count = S.count('0')
        one_count = len(S) - zero_count
        diff = abs(zero_count - one_count)
        if diff > 0:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    solve()
