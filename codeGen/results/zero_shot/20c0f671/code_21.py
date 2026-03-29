import sys

books = []
max_shelf_width = 0

# Read input from stdin
for line in sys.stdin:
    thickness, height = map(int, line.strip().split())
    books.append((thickness, height))

shelves = []

books.sort(key=lambda x: x[1], reverse=True)

current_shelf = {'books': [], 'max_height': 0}
shelves.append(current_shelf)

for book in books:
    min_shelf = None
    for i, s in enumerate(shelves):
        if len(s['books']) == 0 and book[0] <= s['max_width']:
            s['books'].append(book)
            shelves[i]['max_height'] = max([b[1] for b in s['books']])
            min_shelf = s
            break
    if min_shelf is None:
        current_shelf = {'books': [book], 'max_height': book[1]}
        shelves.append(current_shelf)

total_height = sum([s['max_height'] for s in shelves])
print(total_height)
