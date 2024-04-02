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


class PseudoQueue:
    """A FIFO Pseudo Queue made using two stacks to emulate a queue without being one.
    Required methods are as follows:
    enqueue
        Arguments: value
        Inserts a value into the PseudoQueue, using a first-in, first-out approach.
    dequeue
        Arguments: none
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
    """

    # Define 2 stacks, In Stack and Out Stack. enqueues will go to the in stack, and
    # dequeues will pull from the outstack (transferring contents of instack if needed)
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    # Push the "enqueued" value into the in_stack.
    def enqueue(self, value):
        self.in_stack.push(value)

    def dequeue(self):

        # Prepare a temp holding value
        transfer_value = 0

        # Instack is empty, so there is no need to pop push to outstack before popping
        # the outstack.
        if self.in_stack.is_empty() == True:

            # Make sure there's anything in the outstack at all first though!
            if self.out_stack.is_empty() == False:
                return self.out_stack.pop()

            #Both stacks empty, return "can't do this on an empty queue" error.
            else:
                raise InvalidOperationError("Method not allowed on empty collection")


        # Instack NOT empty, pop all contents of instack and push them into outstack
        # before proceeding.
        else:
            while self.in_stack.is_empty() == False:

                # Pop from in stack and save returned value...
                transfer_value = self.in_stack.pop()
                # then place value into out_stack with a push. this inverts the stack.
                self.out_stack.push(transfer_value)

            # With that done, pop from the outstack.
            return self.out_stack.pop()
