class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def stringify(head):
    stack = []
    curr = head
    
    while curr is not None:
        stack.append(curr.val)
        curr = curr.next
    
    res = 'null'
    
    while len(stack) > 0:
        res = str(stack.pop()) + ' -> ' + res
    
    return res
