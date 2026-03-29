import sys

def solve(t):
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Sort the sequence and split it into two sub-sequences
        a.sort()
        x = [a[i] for i in range(n) if i % 2 == 0]
        y = [a[i] for i in range(n) if i % 2 != 0]
        
        # Initialize the minimum value of F
        min_f = float('inf')
        
        # Try all possible combinations of x and y to find the minimum value of F
        for i in range(2**len(x)):
            f = 0
            for j in range(len(x)):
                if (x[j] - s) * ((y[-j-1] - s) if j % 2 == 0 else (a[-1] - s)) >= 0:
                    f += x[j] * y[-j-1]
                else:
                    f += x[j] * (a[-1] - s)
            min_f = min(min_f, f)
        
        print(min_f)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    solve(t)
