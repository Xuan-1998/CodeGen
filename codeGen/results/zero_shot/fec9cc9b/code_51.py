def is_ladder(arr, l, r):
    # Check if the subsegment doesn't decrease
    decreasing = False
    for i in range(l, r):
        if arr[i] < arr[i-1]:
            decreasing = True
            break
    
    # If it's not decreasing, check if it doesn't increase
    if not decreasing:
        increasing = False
        for i in range(l+1, r):
            if arr[i] > arr[i-1]:
                increasing = True
                break
    
    return not decreasing and not increasing

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(m):
        l, r = map(int, input().split())
        print("Yes" if is_ladder(arr, l-1, r) else "No")

if __name__ == "__main__":
    main()
