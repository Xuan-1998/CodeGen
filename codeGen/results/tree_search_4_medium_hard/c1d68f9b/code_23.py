def can_form_polygon(moods):
    memo = {(0, False): True}

    def dfs(n, good_mood):
        if (n, good_mood) in memo:
            return memo[(n, good_mood)]
        
        result = False
        for i in range(n):
            if moods[i] % n != 0: 
                continue
            else:
                result = result or good_mood
        
        memo[(n, good_mood)] = result
        return result

    return "YES" if dfs(len(moods), True) else "NO"
