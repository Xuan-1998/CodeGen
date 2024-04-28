from collections import defaultdict

def minUncommonLength(S, T):
    memo = defaultdict(list)
    
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                memo[(i-1, j-1)].append((i, j))
                
    uncommon_lengths = []
    
    for (i, j) in memo:
        uncommon_lengths.append((j-i+1, (i, j)))
        
    uncommon_lengths.sort()
    
    result = 0
    prev_end_index = 0
    
    for length, end_indices in uncommon_lengths:
        start_index, _ = end_indices
        
        if start_index > prev_end_index:
            result += length
            prev_end_index = end_indices[1]
            
    return -1 if result == 0 else result

if __name__ == "__main__":
    S = input()
    T = input()
    
    print(minUncommonLength(S, T))
