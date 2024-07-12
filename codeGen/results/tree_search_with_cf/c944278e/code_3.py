python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    from functools import lru_cache
    
    @lru_cache(None)
    def dp(i, mask):
        if i == n:
            return {mask}
        
        result = set()
        step = 1 << (n - i - 1)
        
        for j in range(0, 2 ** n, 2 * step):
            for k in range(step):
                if s[i] == '0':
                    result |= dp(i + 1, mask & ~(1 << (j + k + step)))
                else:
                    result |= dp(i + 1, mask & ~(1 << (j + k)))
        
        return result
    
    initial_mask = (1 << (2 ** n)) - 1
    possible_max_values = dp(0, initial_mask)
    
    sorted_result = sorted(possible_max_values)
    print(" ".join(map(str, sorted_result)))


