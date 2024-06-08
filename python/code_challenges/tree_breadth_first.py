from data_structures.binary_tree import BinaryTree

def breadth_first(self):

    # Queue is for storing object references for action ordering...
    queue = []
    # While values is used to hold the values of the nodes themselves.
    values = []

    if not self or self.root is None:
        return[]

    queue.append(self.root)

    # if the queue contains anything...
    while len(queue) > 0:

        node = queue.pop(0)
        # Add front of queue node's value to values list
        values.append(node.value)
        # Set self to node reference at front of queue


        # Check if left exists, and if so
        if node.left is not None:
            queue.append(node.left)

        # Check if right exists, and if so
        if node.right is not None:
            queue.append(node.right)

    return values
