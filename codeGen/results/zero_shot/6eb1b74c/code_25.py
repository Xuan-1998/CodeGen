import sys

def check_colored_red(t):
    for char in t:
        if char.lower() != 'x':
            return False
    return True

min_steps = 0
curr_pos = 0

for _ in range(int(input())):
    text = input()
    num_strings = int(input())
    strings = [input() for _ in range(num_strings)]
    
    while not check_colored_red(text):
        min_steps += 1
        curr_pos = 0
        
        for string in strings:
            pos = curr_pos
            while True:
                pos = text.find(string, pos)
                if pos == -1:
                    break
                text = text[:pos] + 'x' * len(string) + text[pos+len(string):]
                curr_pos = pos + 1
    
    print(min_steps)

    for j in range(min_steps):
        w = strings.index(next(s for s in strings if s in text))
        p = text.find(strings[w], 0)
        while True:
            text = text[:p] + 'x' * len(strings[w]) + text[p+len(strings[w]):]
            if not (strings[w] in text):
                break
            p = text.find(strings[w], p+1)
        print(w+1, p+1)
