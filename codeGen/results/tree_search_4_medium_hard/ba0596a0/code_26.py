import sys

def can_cross_stones(stones):
    n = len(stones)
    k = stones[1] - stones[0]
    dp = {(i, 0): True for i in range(n)}
    dp[(n-1, 0)] = False
    
    for j in range(1, n):
        for prev_jump_len in range(min(k, j), max(k, j)+1):
            if (j, prev_jump_len) not in dp:
                dp[(j, prev_jump_len)] = False
                for i in range(j-1, -1, -1):
                    if abs(stones[j] - stones[i]) in [prev_jump_len-1, prev_jump_len, prev_jump_len+1] and dp[(i, prev_jump_len-1)]:
                        dp[(j, prev_jump_len)] = True
                        break
    
    return any(dp[(n-1, j)] for j in range(min(k, n), max(k, n)+1))

if __name__ == "__main__":
    stones = [int(x) for x in sys.stdin.read().split()]
    print(can_cross_stones(stones))
