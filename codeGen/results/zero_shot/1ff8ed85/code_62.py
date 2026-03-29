def can_obtain_b(segments):
    b_str = "".join(str(len(segment)) + str(segment) for segment in segments)
    return b_str == "".join(map(str, b))

result = False
for segments in generate_segments(n, ""):
    if can_obtain_b(segments):
        result = True
        break

print("YES" if result else "NO")
