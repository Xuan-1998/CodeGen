import sys

state = [0, 0, False]  # A count, B count, flag indicating 'AB' found

for c in sys.stdin.readline().strip():
    if c == 'A':
        state[0] += 1
    elif c == 'B':
        state[1] += 1
    if state[0] == 1 and state[1] == 1:
        state[2] = True

if not state[2]:
    return "NO"

window_state = [0, 0]
for c in sys.stdin.readline().strip():
    if c == 'A':
        window_state[0] += 1
    elif c == 'B':
        window_state[1] += 1
    if window_state[0] == 1 and window_state[1] == 1:
        return "YES"
    if window_state[0] == 0 and window_state[1] == 0 and state[2]:
        return "NO"

print("YES")
