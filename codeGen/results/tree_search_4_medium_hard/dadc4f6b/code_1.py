def solve(n, q, c, star_coords, views):
    dp_table = [[0] * (c + 1) for _ in range(q + 1)]

    for i in range(1, q + 1):
        t, x1, y1, x2, y2 = views[i - 1]
        for j in range(min((x2 - x1) // 10, c), -1, -1):
            visible_stars = sum(s_i > 0 and (x1 <= star_coords[k][0] <= x2 or y1 <= star_coords[k][1] <= y2) for k in range(n))
            dp_table[i][j] = max(dp_table[i - 1][j], j * visible_stars + dp_table[i - 1][max(0, j - c)])
        print(dp_table[q][c])

# Example usage:
n = 5
q = 3
c = 10
star_coords = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
views = [(0, 1, 1, 3, 3), (1, 2, 2, 4, 4), (2, 5, 5, 7, 7)]

solve(n, q, c, star_coords, views)
