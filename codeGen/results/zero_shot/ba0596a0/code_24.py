def can_cross(stones):
    stones = list(map(int, input().split()))
    n = len(stones)
    left, right = 0, n - 1
    k = stones[1] - stones[0]
    
    while left <= right:
        if abs(stones[right] - stones[left]) > k * 2 + 1:
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    print(can_cross(input()))
