def max_common_substrings(str1, str2):
    N = len(str1)
    if N != len(str2):
        return 0
    
    max_count = 0
    seen = set()
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            substr = str1[i:j+1]
            
            if substr in seen:
                continue
                
            common = True
            for k in range(N):
                if str1[k] != str2[k] and str1[k:k+len(substr)] == substr:
                    common = False
                    break
                    
            if common:
                max_count += 1
                seen.add(substr)
                
    return max_count
