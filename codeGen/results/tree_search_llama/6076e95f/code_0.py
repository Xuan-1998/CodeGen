def sequence(start, end):
    def recurse(current, cache={}):
        if current > end:
            return []
        if current in cache:
            return cache[current]
        result = [current] + recurse(current + 1, cache)
        cache[current] = result
        return result
    
    return recurse(start)

# Read input from stdin
start, end = map(int, input().split())

# Generate the sequence and print it to stdout
print(" ".join(map(str, sequence(start, end))))
