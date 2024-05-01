import sys

def solve():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    # Preprocess characters to distinct values (0 for *, 1 for #, and 2 for @)
    mapping = {c: i for i, c in enumerate(set(str1 + str2))}
    
    # Initialize dictionary to store unique substrings and their frequencies
    freq_dict = {}
    
    # Generate all possible substrings of both input strings
    for i in range(N):
        for j in range(i + 1, N + 1):
            sub_str1 = str1[i:j]
            sub_str2 = str2[i:j]

            # Check if the substring appears in both input strings
            if all(mapping[c] == mapping[cs] for c, cs in zip(sub_str1, sub_str2)):
                # Increment frequency of this unique substring
                freq_dict[sub_str1] = freq_dict.get(sub_str1, 0) + 1
    
    # Find the maximum frequency among unique substrings
    max_freq = max(freq_dict.values(), default=0)
    
    print(max_freq)

if __name__ == "__main__":
    solve()
