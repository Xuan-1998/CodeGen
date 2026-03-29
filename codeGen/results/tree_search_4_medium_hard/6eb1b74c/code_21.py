import sys

def process():
    dp = [[float('inf')] * (len(input()) + 1) for _ in range(len(open_files)+ 1)]
    
    for j in range(1, len(open_files) + 1):
        for i in range(len(input()) - open_files[j-1].length + 1):
            if input()[i:i+len(open_files[j-1])] == open_files[j-1]:
                dp[j][i] = min(dp[j-1][i], 1 + dp[0][i+len(open_files[j-1])])
            else:
                dp[j][i] = dp[j-1][i]
                
    m = dp[-1][-1]
    
    if m == float('inf'):
        print(-1)
    else:
        print(m)
        
        for j in range(1, m+1):
            for i in range(len(input()) - ''.join(open_files[:j]).length + 1):
                if input()[i:i+len(''.join(open_files[:j]))]) == ''.join(open_files[:j]):
                    print(j, i)

process()
