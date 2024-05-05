def color_text(text_left, strings_used):
    if not text_left:
        return 0
    if strings_used == len(strings):
        return float('inf')
    
    dp = {(text_left, i): None for i in range(len(strings))}
    for (text_left, strings_used) in [(text_left[i:], strings_used) for i in range(len(text_left))]:
        if strings_used > 0:
            min_steps = float('inf')
            for j, string in enumerate(strings):
                if text_left.startswith(string):
                    steps = color_text(text_left[len(string):], strings_used - (j + 1))
                    if steps is not None:
                        min_steps = min(min_steps, steps) + 1
            dp[(text_left, strings_used)] = min_steps if min_steps != float('inf') else -1
        else:
            dp[(text_left, strings_used)] = -1
    
    return dp.get((text_left, strings_used), -1)

while True:
    n = int(input())
    if not n:
        break
    text = input()
    strings = [input() for _ in range(n)]
    
    min_steps = color_text(text, 0)
    if min_steps == -1:
        print(-1)
    else:
        steps = []
        curr_text = text
        curr_strings_used = 0
        while True:
            min_str_idx = None
            min_start = float('inf')
            for i, string in enumerate(strings):
                if i not in range(curr_strings_used) and curr_text.startswith(string):
                    start = curr_text.find(string)
                    if start < min_start:
                        min_str_idx = i
                        min_start = start
            if min_str_idx is None:
                break
            steps.append((min_str_idx, min_start))
            curr_text = curr_text[min_start + len(strings[min_str_idx]):]
            curr_strings_used += 1
        
        print(min_steps)
        for step in steps:
            print(step[0], step[1])
