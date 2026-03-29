import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    
    # Create a hash table to store the frequencies of substrings
    freq = {}
    
    # Count the frequency of each substring in the original string
    for i in range(len(s) - k + 1):
        sub = s[i:i+k]
        freq[sub] = freq.get(sub, 0) + 1
    
    # Count the frequency of each substring in the infinite string
    inf_freq = {}
    last_k_chars = s[-k:]
    for i in range(len(last_k_chars)):
        inf_sub = last_k_chars[i:i+k]
        inf_freq[inf_sub] = inf_freq.get(inf_sub, 0) + 1
    
    # Calculate the minimum number of characters that need to be changed
    min_changes = 0
    for sub, count in freq.items():
        if sub not in inf_freq or count != inf_freq[sub]:
            min_changes += count - max(count, inf_freq.get(sub, 0))
    
    print(min_changes)

if __name__ == "__main__":
    solve()
