import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        p_a = []
        p_b = []
        for _ in range(n):
            p, a, b = map(float, sys.stdin.readline().split())
            p_a.append((p, a))
            p_b.append((p, b))
        
        # Calculate the probability of each ticket having a unique number
        probability = 1.0
        for i in range(n):
            pa, _ = p_a[i]
            pb, _ = p_b[i]
            if pa >= pb:
                probability *= (pa / (pa + pb))
            else:
                probability *= (pb / (pa + pb))
        
        print(f"{probability:.6f}")  # Print the result with precision 10^-6

calculate_probability()
