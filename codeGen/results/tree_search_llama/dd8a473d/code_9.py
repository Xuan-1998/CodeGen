# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> null
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print(stringify(head))  # Output: "1 -> 2 -> 3 -> 4 -> null"
