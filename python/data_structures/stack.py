from data_structures.invalid_operation_error import InvalidOperationError
# ? Node recycled from linked_list.py from this directory.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class Stack:
    """
    Basic LIFO stack system. Uses a singly linked list format as it's base structure.
    has methods:
    is_empty() returning boolean
    push(value) returning nothing
    pop() returning popped value
    peek() returning value from topmost node.
    """

    # Initialize stack with a null reference instead of a node at the top.
    def __init__(self):
        self.top = None

    # Self.top is None will result in a true or false depending on if stack exists.
    def is_empty(self):
        return self.top is None

    # Add a new node to the top of the stack.
    def push(self, value):

        # Is the stack empty with a null reference at the top? if so, set top to Node.
        if self.top == None:
            self.top = Node(value)

        # Define a new node, set it's next to point to the current top, and then
        # set the top to be the newly pushed node.
        else:
            pushed_node = Node(value, self.top)
            self.top = pushed_node

    def pop(self):

        # Empty stack error handling. If self.top.value doesn't exist, stack's empty.

        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        else:
            requested_node = self.top
            # Move current top's next to the top.
            self.top = self.top.next
            # Provide .value of popped node.
            return requested_node.value

    def peek(self):
        # empty stack error handling

        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value
