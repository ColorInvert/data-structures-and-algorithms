# ? Linked list implementation greatly assisted by Fakorede Damilola's Linked Lists in Python – Explained with Examples.


class TargetError:
    pass


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        old_head = self.head
        new_head_val = value
        new_node = Node(new_head_val, old_head)
        self.head = new_node

    def traverse(self):
        current = self.head
        while current is not None:
            # print(current.value)
            current = current.next

    def includes(self, value):
        target = value
        current = self.head
        # For as long as we're not at the end of the list...
        while current is not None:
            # Check if the current head node holds a value equal to target. if so, target found.
            if target == current.value:
                return True
            # If not, look at the next node.
            else:
                current = current.next

        # While Loop breaks if end of LL is reached, meaning target is not present. return false.
        return False

    def to_string(self):
        current = self.head
        ll_contents = []
        my_string = "{ "
        # For as long as we're not at the end of the list...
        while current is not None:
            # append the current value to the list of LL values.
            ll_contents.append(current.value)
            # move to next.
            current = current.next

        # ? Vestige of my "test_to_string_captures_values()" pytest.
        # return ll_contents

        # assemble a { 3 } -> { 2 } -> { 1 } -> { formatted string
        for i in ll_contents:
            my_string += f"{i} }} -> {{ "
            pass

        # get rid of last "{" and replace it with "NULL"
        my_string = my_string.rstrip("{ ")
        my_string += " NULL"
        return my_string

    # Add a new node with a given value to the end of the list.
    def append(self, value):
        current = self.head

        # Advance through the list until the next node is null, indicating the end.
        while current.next is not None:
            current = current.next

        # change the "next" value of the last node to a freshly created node.
        current.next = Node(value)

        # Tell user of success.
        return f"New node with a value of {value} added to end of linked list."

    # Add a new node with a given new_value immediately before the node that has the value provided.
    def insert_before(self, value, new_value):
        current = self.head

        # check if, and run insert method instead, if the value provided is the head.
        if current.value == value:
            self.insert(new_value)
            return f"New node with a value of {new_value} placed before the first instance of {value} (which was the head!)."

        # Advance through the list until the next node is the target value.
        while current.next.value is not value:
            current = current.next

        #!error handling if insert_before's value is not present in the linked list.
        if current.next is None:
            return f"requested value of {value} to insert {new_value} before not found!"

        # From the node immediately before the one we're looking for, create a new node that has a matching next destination of our existing node, and then overwrite this previous node's next value with the freshly created node, forcing it between the two.
        new_node = Node(new_value, current.next)
        current.next = new_node

        # Tell user of success.
        return f"New node with a value of {new_value} placed before the first instance of {value}."

    # Add a new node with a given new_value immediately after the node that has the value provided.
    def insert_after(self, value, new_value):
        current = self.head

        # Advance through the list until we are on the node containing the requested value.
        while current.value is not value:
            current = current.next

        #!error handling if insert_after's value is not present in the linked list.
        if current is None:
            return f"requested value of {value} to insert {new_value} after not found!"

        new_node = Node(new_value, current.next)
        current.next = new_node

        # Tell user of success.
        return f"New node with a value of {new_value} placed after the first instance of {value}."

    # Returns the value for the node k number of steps back from the final node. Note that k is measured in steps taken, so k=0 is the last node, and k = 1 is one step back!
    def kthFromEnd(self, k):
        current = self.head
        values_list = []

        # Traverse linked list, saving each node's value to a list
        while current.next is not None:
            values_list.append(current.value)
            current = current.next

        # Get the last node's value since the loop breaks before it is saved.
        values_list.append(current.value)

        # !Error handling for k being bigger than ll node count.
        if k >= len(values_list):
            return "Exception"
        # !Error handling for negative value for k.
        elif k < 0:
            return "Exception"

        values_list.reverse()
        return values_list[k]


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# ? to insert at the start of a linked list, new node must be created, new node must link to existing head, head must be re-assigned to new node.


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.insert(20)
    print(ll.includes(10))
