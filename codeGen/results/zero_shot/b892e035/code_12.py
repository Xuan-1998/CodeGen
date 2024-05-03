import sys

def prob_correct_numbering():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probs = []
        nums = []
        for _ in range(n):
            p, a, b = map(float, sys.stdin.readline().split())
            probs.append(p)
            nums.append((a, b))
        
        # Calculate the total probability
        P = 1.0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i][0] != nums[j][0] and nums[i][0] != nums[j][1]:
                    P *= probs[i] * (1 - probs[i]) * probs[j]
        
        print(round(P, 6))  # Round to 10^-6 precision

prob_correct_numbering()
