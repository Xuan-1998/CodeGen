from collections import defaultdict

def count_bear_pairs():
    s = input()
    bear_indices = defaultdict(list)
    
    for i in range(len(s)):
        if s[i:i+4] == 'bear':
            bear_indices[i].append(i)
    
    pairs_count = 0
    
    for start in bear_indices:
        for end in bear_indices[start:]:
            if start < end:
                pairs_count += 1
            else:
                break
            
    print(pairs_count)

count_bear_pairs()
