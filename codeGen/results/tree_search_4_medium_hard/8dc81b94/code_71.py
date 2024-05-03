===BEGIN CODE===
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Calculate prefix sum
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
        
    # Calculate suffix sum
    suffix_sum = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i]
        
    # Check if it's possible to make all elements equal to zero
    if prefix_sum[-1] == suffix_sum[0]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
===END CODE===
