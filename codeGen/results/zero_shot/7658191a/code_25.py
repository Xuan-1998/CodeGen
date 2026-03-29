def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        score = 0
        moves_left = k
        left_moves = 0
        
        for i in range(1, n+1):
            if moves_left > 0:
                # try to move to the right
                score += arr[i-1]
                moves_left -= 1
            elif left_moves < z and arr[i-1] >= arr[i]:
                # try to move to the left (but not too many)
                score += arr[i-1]
                left_moves += 1
                if left_moves == z:
                    break
        
        print(score)

if __name__ == "__main__":
    solve()
