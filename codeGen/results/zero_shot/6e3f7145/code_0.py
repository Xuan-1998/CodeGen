def longest_palindrome(S):
    n = len(S)
    max_len = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            if S[i:j+1] == S[i:j+1][::-1]:
                if len(S[i:j+1]) > max_len:
                    max_len = len(S[i:j+1])
                    result = S[i:j+1]
    
    print(result)
