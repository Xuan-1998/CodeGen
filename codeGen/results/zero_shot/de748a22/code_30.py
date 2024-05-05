def solve():
    n, q = map(int, input().split())
    arr = list(input())
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + (-1 if arr[i] == '-' else 1)
    
    total_signs = 0
    min_removals = float('inf')
    
    for _ in range(q):
        l, r = map(int, input().split())
        
        remaining_signs = prefix_sum[r+1] - prefix_sum[l]
        
        if remaining_signs != 0:
            total_signs += abs(remaining_signs)
            
            min_removals = min(min_removals, total_signs)
    
    print(min_removals)

if __name__ == "__main__":
    solve()
