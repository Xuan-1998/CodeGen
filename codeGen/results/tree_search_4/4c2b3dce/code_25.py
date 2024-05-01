def solve():
    s = input()
    n = len(s)
    
    # Split the string into two halves
    half = n // 2
    
    # Check if both 'AB' and 'BA' appear in each half
    return ("YES" if check_substring(s[:half]) and check_substring(s[half:]) else "NO")

def check_substring(s):
    last_char, remaining_string = None, s
    for i, char in enumerate(remaining_string):
        # Check if 'AB' or 'BA' appears at the current position
        if (last_char == 'B' and char == 'A') or (last_char == 'A' and char == 'B'):
            return True
        last_char = char
    return False

print(solve())
