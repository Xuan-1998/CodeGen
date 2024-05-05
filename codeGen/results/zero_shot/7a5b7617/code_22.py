import sys

def solve():
    T = int(input())
    results = []
    
    for _ in range(T):
        N, M = map(int, input().split())
        total_sum = (N-1) * M
        if N > 2:
            total_sum += (N-2) * min(N-1, M)
        
        results.append(total_sum % 1000000000)

    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
