import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k, z = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Calculate the maximum score that can be achieved
        max_score = 0
        for i in range(k):
            if i < z:
                max_score += arr[i]
            else:
                max_score += arr[k - (i - z + 1)]
                
        print(max_score)

if __name__ == "__main__":
    solve()
