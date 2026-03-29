import sys
from math import comb

def main():
    n = int(sys.stdin.readline().strip())
    prob = 1
    for i in range(n):
        prob *= (n-i) // (i+1)
    print(prob % 998244353)

if __name__ == "__main__":
    main()
