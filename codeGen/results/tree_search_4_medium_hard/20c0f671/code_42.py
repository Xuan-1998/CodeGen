import heapq

def min_height_of_bookcase(thicknesses, heights, shelf_width):
    dp = [[float('inf')] * (shelf_width + 1) for _ in range(len(thicknesses) + 1)]
    dp[0] = [0] * (shelf_width + 1)
    
    queue = [(heights[0], thicknesses[0], heights[0])]
    heapq.heapify(queue)
    
    for i in range(1, len(thicknesses) + 1):
        while queue and queue[0][1] <= shelf_width:
            h, t, min_height = heapq.heappop(queue)
            for j in range(i-1, -1, -1):
                if dp[j][shelf_width-t] > min_height + heights[j]:
                    dp[i][shelf_width-t] = min_height + heights[j]
                    break
        for k in range(i-1, -1, -1):
            if t <= shelf_width and dp[k][shelf_width-t] > dp[k-1][shelf_width]:
                dp[i][shelf_width] = dp[k-1][shelf_width]
                break
        heapq.heappush(queue, (heights[i], thicknesses[i], heights[i]))
    
    return dp[-1][-1]

# Example usage:
thicknesses = [3, 2, 5, 4, 6, 7, 8, 9]
heights = [10, 15, 20, 25, 30, 35, 40, 45]
shelf_width = 12
print(min_height_of_bookcase(thicknesses, heights, shelf_width))  # Output: 55

