===BEGIN SOLUTION===
import sys

s = sys.stdin.readline().strip()

state = {'A': False, 'B': False}
found_A = found_B = False

for char in s:
    if char == 'A':
        state['A'] = not state['A']
        found_A = True
    elif char == 'B' and found_A:
        state['B'] = not state['B']
        found_B = True

result = (state['A'] and state['B'])
if result:
    print("YES")
else:
    print("NO")
===END SOLUTION===
