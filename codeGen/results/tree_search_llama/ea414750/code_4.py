def count_bear_pairs():
    s = input()
    bear_occurrences = set()
    
    for i in range(len(s) - 3):
        if s[i:i+4] == 'bear':
            bear_occurrences.add(i)
    
    pairs_count = 0
    
    for i in bear_occurrences:
        for j in range(i, len(s) - 3):
            if s[j:j+4] == 'bear' and i <= j:
                pairs_count += 1
                break
    
    print(pairs_count)

if __name__ == "__main__":
    count_bear_pairs()
