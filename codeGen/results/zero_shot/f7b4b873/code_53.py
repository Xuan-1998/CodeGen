import sys

def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitions(S):
    N = len(S)
    partitions = []
    
    for i in range(N+1):
        for j in range(i, N+1):
            partition = S[i:j]
            
            if is_palindrome(partition):
                if any(p not in [partition] for p in partitions):
                    partitions.append([partition])
                else:
                    continue
            else:
                break
        
    return partitions

if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    print(palindromic_partitions(S))
