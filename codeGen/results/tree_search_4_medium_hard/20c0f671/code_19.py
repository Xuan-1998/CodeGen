def min_height_of_bookcase(books, max_shelf_width):
    dp = {}
    
    for j in range(len(books) + 1):
        for k in range(max_shelf_width + 1):
            if j == 0:
                dp[(j, k)] = 0
            elif k < books[j-1][0]:
                dp[(j, k)] = dp[(j-1, k)]
            else:
                dp[(j, k)] = min(dp.get((i, min(k, w)), float('inf')) + h for i, (w, h) in enumerate(books[:j]))
                
    return dp[(len(books), max_shelf_width)]

# Example usage
books = [(2, 5), (3, 4), (1, 3)]
max_shelf_width = 6

print(min_height_of_bookcase(books, max_shelf_width))
