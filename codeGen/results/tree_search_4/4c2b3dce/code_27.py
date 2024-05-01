dp = {}

def solve(last_char, remaining_string):
    if (last_char, remaining_string) in dp:
        return dp[(last_char, remaining_string)]

    if not remaining_string:
        return True

    if last_char == 'A' and remaining_string[0] == 'B':
        result = solve('B', remaining_string[1:])
        dp[(last_char, remaining_string)] = result
        return result

    if last_char == 'B' and remaining_string[0] == 'A':
        result = not solve('A', remaining_string[1:])
        dp[(last_char, remaining_string)] = result
        return result

    dp[(last_char, remaining_string)] = False
    return dp[(last_char, remaining_string)]

s = input()
print("YES" if solve(' ', s) else "NO")
