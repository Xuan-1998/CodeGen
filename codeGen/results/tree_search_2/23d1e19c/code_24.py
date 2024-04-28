from collections import defaultdict

def min_max_recomputations(edges, path):
    n = len(path)
    memo = defaultdict(lambda: (float('inf'), float('-inf')))

    def dfs(v, prev_v, prev_path):
        if v == n:
            return 0, 0
        if (prev_v, prev_path) in memo:
            rec_min, rec_max = memo[(prev_v, prev_path)]
            return rec_min, rec_max

        rec_min = float('inf')
        rec_max = float('-inf')

        for next_v in [u for u, v_edge in edges.items() if v_edge == v]:
            if next_v == path[0]:  # part of the fixed path
                rec_min = min(rec_min, dfs(next_v, v, prev_path + [v]).min)
                rec_max = max(rec_max, dfs(next_v, v, prev_path + [v]).max)
            else:  # recompute shortest path
                next_rec_min = float('inf')
                next_rec_max = float('-inf')
                for t in range(n):
                    if path[t] == next_v:
                        break
                    next_rec_min = min(next_rec_min, dfs(t, v, prev_path + [v]).min)
                    next_rec_max = max(next_rec_max, dfs(t, v, prev_path + [v]).max)

                rec_min = min(rec_min, 1 + next_rec_min)
                rec_max = max(rec_max, 1 + next_rec_max)

        memo[(prev_v, prev_path)] = (rec_min, rec_max)
        return rec_min, rec_max

    return dfs(0, None, []).min, dfs(0, None, []).max
