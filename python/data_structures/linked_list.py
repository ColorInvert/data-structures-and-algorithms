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
