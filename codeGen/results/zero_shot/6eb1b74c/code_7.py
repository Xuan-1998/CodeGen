def min_steps(t, s):
    steps = 0
    used_strings = []
    
    for i in range(len(t)):
        for j in range(i+1, len(t)+1):
            substring = t[i:j]
            if any(substring == string for string in s):
                if substring not in used_strings:
                    used_strings.append(substring)
                    steps += 1
                    break
    
    return steps

# Read input from stdin
t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]

# Print the minimum number of steps and how to do it
print(min_steps(t, s))
