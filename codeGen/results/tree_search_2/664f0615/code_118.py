def max_path_length(v0, vf, tmax, dv):
    dp = {(v0, 1): 0}  # Initialize memoization dictionary

    for t in range(2, tmax + 1):
        for v in range(min(v0, vf), max(v0, vf) + 1):
            if abs(v - v0) <= dv and abs(v - vf) <= dv:
                dp[(v, t)] = min(dp.get((v0, t - 1), float('inf')), dp.get((vf, t - 1), float('inf'))) + v

    return max(dp.values())

# Example usage
v0, vf, tmax, dv = map(int, input().split())
print(max_path_length(v0, vf, tmax, dv))
