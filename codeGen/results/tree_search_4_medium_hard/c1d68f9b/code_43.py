def can_form_polygon(n, moods):
    memo = {}
    
    def dp(s):
        if len(s) == n - 1:
            return True
        if s in memo:
            return memo[s]
        
        result = False
        for i in range(len(s)):
            if moods[s[i]] == 1:  # good mood
                new_s = set(s).union({i})
                if dp(new_s):
                    result = True
                    break
        
        memo[s] = result
        return result
    
    for i in range(n):  # iterate over all possible states
        s = set()
        for j in range(i, n):
            s.add(j)
            if not dp(s):
                return "NO"
    
    return "YES"

# Example usage:
n = int(input())
moods = [int(x) for x in input().split()]
print(can_form_polygon(n, moods))
