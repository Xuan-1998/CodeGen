code
import sys

def solve():
    while True:
        n, q = map(int, input().split())
        signs = list(input())

        for _ in range(q):
            l, r = map(int, input().split())
            total_sum = 0
            for i in range(l-1, r):
                total_sum += -1 if signs[i] == '+' else 1

            min_remove = 0
            current_sum = 0
            for i in range(r-l+1):
                current_sum += -1 if signs[l-1+i] == '+' else 1
                if current_sum < 0:
                    min_remove = r-l + 1 - i
                    break

            print(min_remove)

if __name__ == "__main__":
    solve()
