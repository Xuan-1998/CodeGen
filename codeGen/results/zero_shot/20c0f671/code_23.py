thicknesses, heights, shelf_width = [list(map(int, input().split())) for _ in range(3)]
books = sorted(zip(heights, thicknesses), key=lambda x: x[0], reverse=True)
heights, thicknesses = zip(*books)
shelves = [[], 0]
shelf_width = sum(thicknesses) + thicknesses[0] if thicknesses else 0
total_height = 0
for h, t in books:
    if t <= shelf_width:
        shelves[-1].append((h, t))
        shelf_width = sum(t for _, t in shelves[-1])
    else:
        shelves.append([(h, t), 0])
        shelf_width = t
total_height = max(h for h, _ in shelves)
print(total_height)
