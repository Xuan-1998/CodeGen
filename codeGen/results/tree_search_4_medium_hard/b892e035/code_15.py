import sys

def probability():
    t = int(input())
    for _ in range(t):
        n = int(input())
        memo = {}
        for _ in range(n):
            p1, a1, b1 = map(float, input().split())
            p2, a2, b2 = map(float, input().split())
            for state in range(1 << 16):  # all possible states
                count = 0
                for i in range(8):
                    if (state >> i) & 1:  # if bit is set
                        count += 1
                memo[state] = min(count, n - count)
        print(min(memo.values()))  # probability of correct numbering

if __name__ == "__main__":
    probability()
