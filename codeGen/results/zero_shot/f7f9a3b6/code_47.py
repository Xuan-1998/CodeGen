def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]
    
    prefix_sum = [0] * 27
    for i, c in enumerate(s):
        prefix_sum[ord(c) - ord('a') + 1] += 1
    
    ways = 0
    max_len = 0
    min_substrings = n
    for start in range(n):
        curr_max_len = 0
        count = [0] * 27
        end = start
        while end < n:
            for char, val in zip(s[start:end+1], prefix_sum[ord(c) - ord('a') + 1]):
                if val > a[ord(char) - ord('a')]:
                    break
            else:
                curr_max_len += (end - start + 1)
                end = n
            end += 1
        
        if curr_max_len > max_len:
            max_len = curr_max_len
        ways += 1
        min_substrings = min(min_substrings, curr_max_len)
    
    print(ways % (10**9 + 7))
    print(max_len)
    print(min_substrings)

if __name__ == '__main__':
    solve()
