import sys

def solve():
    n = int(input())
    text = input()
    strings_to_positions = {}
    
    for _ in range(n):
        string = input()
        if string not in strings_to_positions:
            strings_to_positions[string] = []
        positions = [i for i, char in enumerate(text) if char == string[0]]
        strings_to_positions[string].extend(positions)
    
    dp = [float('inf')] * (len(text) + 1)
    dp[0] = 0
    
    for i in range(1, len(text) + 1):
        min_steps = float('inf')
        for string, positions in strings_to_positions.items():
            if any(pos <= i for pos in positions):
                steps = dp[pos - 1] + 1
                min_steps = min(min_steps, steps)
        
        dp[i] = min_steps
    
    m = dp[-1]
    
    print(m)
    
    for i in range(len(text) - 1, -1, -1):
        if dp[i] != float('inf'):
            string = next(string for string, positions in strings_to_positions.items() if any(pos <= i for pos in positions))
            print(i + 1, len(text) - m)
            m -= 1
