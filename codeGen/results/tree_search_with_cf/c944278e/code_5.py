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
        if i == 0:
            return {mask + 1}
        
        new_set = set()
        half = 2 ** (n - i)
        
        for j in range(0, 2 ** n, half * 2):
            for k in range(half):
                left = mask & (1 << (j + k))
                right = mask & (1 << (j + k + half))
                
                if s[i - 1] == '0':
                    if left:
                        new_set.update(dp(i - 1, mask ^ (1 << (j + k))))
                    if right:
                        new_set.update(dp(i - 1, mask ^ (1 << (j + k + half))))
                else:
                    if left and right:
                        new_set.update(dp(i - 1, mask ^ (1 << (j + k))))
                        new_set.update(dp(i - 1, mask ^ (1 << (j + k + half))))
                    elif left:
                        new_set.update(dp(i - 1, mask ^ (1 << (j + k))))
                    elif right:
                        new_set.update(dp(i - 1, mask ^ (1 << (j + k + half))))
        
        return new_set
    
    result_set = dp(n, (1 << (2 ** n)) - 1)
    result_list = sorted(result_set)
    
    print(" ".join(map(str, result_list)))

if __name__ == "__main__":
    main()

