python
def main():
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
        
        next_mask_set = set()
        step = 1 << (n - i - 1)
        
        for m in range(1 << (n - i)):
            if mask & (1 << (2 * m)):
                if s[i] == '0':
                    next_mask_set.add(m)
                else:
                    next_mask_set.add(m + step)
            if mask & (1 << (2 * m + 1)):
                if s[i] == '0':
                    next_mask_set.add(m)
                else:
                    next_mask_set.add(m + step)
        
        result = set()
        for nm in next_mask_set:
            result.update(dp(i + 1, nm))
        
        return result
    
    initial_mask = (1 << (2 ** n)) - 1
    final_result = dp(0, initial_mask)
    
    print(' '.join(map(str, sorted(final_result))))

if __name__ == "__main__":
    main()

