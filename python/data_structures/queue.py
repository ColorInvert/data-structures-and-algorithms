from data_structures.invalid_operation_error import InvalidOperationError

# ? Node recycled from linked_list.py from this directory.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Basic FIFO queue system. Uses a singly linked list format as it's base structure.

    Adapted/edited from my work in stack.py in this directory/
    has methods:
    is_empty() returns boolean on if queue contains no nodes.
    enqueue(value) returns nothing. adds node to back of queue with value.
    dequeue()  removes node from front of queue, and returns its value/
    peek() returns value at front of queue.
    """

    def __init__(self):
        self.front = None
        self.back = None

    # Self.front is None will result in a true or false depending on if queue exists.
    def is_empty(self):
        return self.front is None

    # Add a new node to the back of the queue.
    def enqueue(self, value):
        new_node = Node(value)

        # Check if the queue is empty, and if it is, set the enqueued node to the front
        # and back of the queue.
        if self.back is None:

            self.back = new_node
            self.front = new_node

        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):

        # Empty queue error handling. If self.front.value doesn't exist, queue's empty.

        if self.is_empty():
            raise InvalidOperationError


        if self.front != self.back:
            requested_node = self.front
            # Move current front's next to the front.
            self.front = self.front.next
            # Provide .value of dequeued node.
            return requested_node.value

        if self.front == self.back:
            requested_node = self.front
            self.front = None
            self.back = None
            return requested_node.value

    def peek(self):
        # empty queue error handling
        if self.is_empty():
            raise InvalidOperationError

        else:
            return self.front.value
