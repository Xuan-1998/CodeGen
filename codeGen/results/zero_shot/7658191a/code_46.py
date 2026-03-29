import sys

def solve():
    n = int(input())
    k = int(input())
    z = int(input())
    arr = list(map(int, input().split()))
    
    max_score = 0
    
    for _ in range(k):
        score = 0
        for i in range(1, n):
            prev_score = score
            if z > 0 and score >= prev_score:
                score += arr[i - 1]
                z -= 1
            else:
                score += arr[i]
        max_score = max(max_score, score)
    
    print(max_score)

if __name__ == "__main__":
    solve()
