python
def min_recolors(n, colors):
    DP = {(i, c) if i == 0 else (0, False): float('inf') for i, c in enumerate(colors)}
    DP[(0, False)] = 0

    for lamp_index in range(1, n):
        same_color = colors[lamp_index] == colors[lamp_index - 1]
        prev_state = (lamp_index - 1, same_color)
        if not same_color:
            DP[(lamp_index, same_color)] = min(DP[prev_state], 1 + DP.get((0, False), float('inf')))
        else:
            DP[(lamp_index, same_color)] = 1 + DP[prev_state]

    return DP[(n - 1, colors[-1] != colors[-2])].item()

n = int(input())
colors = input()
print(min_recolors(n, colors))
