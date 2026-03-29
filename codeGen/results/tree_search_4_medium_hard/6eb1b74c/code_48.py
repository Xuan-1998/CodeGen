import heapq
from collections import defaultdict

def min_steps_to_color_red(text, strings):
    memo = defaultdict(int)
    queue = []

    # Initialize priority queue with all substrings of length 1
    for i in range(len(text)):
        queue.append((0, i, text[i]))

    while queue:
        steps, pos, char = heapq.heappop(queue)

        if pos >= len(text) or text[pos] != char:  # End of the string or mismatched character
            continue

        # Find minimum number of steps for this substring
        min_steps = float('inf')
        for string in strings:
            if string.startswith(char):  # Can we use this string to color?
                new_pos, new_char = pos + len(string), ''
                while new_pos < len(text) and text[new_pos] == char:  # Continue coloring as long as the character matches
                    new_pos += len(string)
                    new_char += string

                if new_char:  # Did we successfully color the substring?
                    new_steps = steps + 1
                    if new_pos < len(text):  # If there are more characters to color, add them to the queue
                        for i in range(new_pos, len(text)):
                            heapq.heappush(queue, (new_steps, i, text[i]))
                    else:
                        min_steps = min(min_steps, new_steps)
                else:  # Couldn't color this substring
                    break

        if min_steps == float('inf'):  # Impossible to color the string red
            return -1

        memo[pos] = min_steps
        for i in range(pos + len(string), len(text)):
            heapq.heappush(queue, (min_steps, i, text[i]))

    return sum(memo.values())

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        text = input()
        n = int(input())
        strings = [input() for _ in range(n)]
        print(min_steps_to_color_red(text, strings))
