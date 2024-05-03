===BEGIN PLAN===
dp = {}

def can_make_zero(arr):
    n = len(arr)
    
    # Base case: empty array is already zero
    if n == 0:
        return True
    
    # If array has only one element, it cannot be made zero
    if n == 1:
        return False
    
    # Calculate the difference between first and last elements
    diff = arr[0] - arr[n-1]
    
    # If difference is increasing, make all elements at end zero and recurse on remaining array
    if diff > 0:
        dp[(n,) + (0,) * n] = can_make_zero(arr[1:])
        
    # If difference is decreasing, make all elements at start zero and recurse on remaining array
    elif diff < 0:
        dp[(0,) * n + (n,) + arr[1:]] = can_make_zero(arr[:-1])
    
    # If difference is zero, either make all elements at end or start zero and recurse on remaining array
    else:
        dp[(n,) + (0,) * n] = can_make_zero(arr[1:])
        dp[(0,) * n + (n,) + arr[1:]) = can_make_zero(arr[:-1])
    
    return dp.get((0,) * n + (n,) * n) or True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print("YES" if can_make_zero(arr) else "NO")

main()
