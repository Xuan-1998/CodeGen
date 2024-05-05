import sys

def color_text(text, strings):
    # Initialize the result
    result = []
    steps = 0
    
    # Loop until all characters are colored
    while any(c.lower() not in [s.lower() for s in strings] for c in text.lower()):
        # Find the first occurrence of a string in the text that hasn't been covered yet
        for i, (t_c, s) in enumerate(zip(text.lower(), strings)):
            if t_c in s:
                result.append((i + 1, text.index(s[0].lower())))
                steps += 1
                break
    
    # If all characters are colored, return the result and number of steps
    if all(c.lower() in [s.lower() for s in strings] for c in text.lower()):
        print(steps)
        for i, (w, p) in enumerate(result):
            print(f'{w} {p}')
    else:
        print('-1')

# Read input from stdin
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Call the function with the input
print(color_text(text, strings))
