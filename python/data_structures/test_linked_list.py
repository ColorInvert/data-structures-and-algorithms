from linked_list import Node
from linked_list import LinkedList


# ?Can we make a node?
def test_node_1():
    actual = Node(1)
    expected = 1
    assert actual.value == expected


# ?Can we make a node that points to another?
def test_node_next():
    node1 = Node(1)
    node2 = Node(2, node1)
    actual = node2.next
    expected = node1
    assert actual == expected


# ?Check for a none error when getting the head of a created list. if an error is caught when trying, none_error becomes true, which is what the assert is looking for.
def test_create_empty():
    my_list = LinkedList()
    try:
        actual = my_list.head()
    except:
        none_error = True

    assert none_error == True


# ? When we make a linked list and call the method insert with a value, is a new node with that value put into the linked list as the head?
def test_insert_adds_to_start():
    my_list = LinkedList()
    my_list.insert(23)

    actual = my_list.head.value
    expected = 23
    assert actual == expected


# ? When we make a linked list and call the method insert with a value multiple times, is hte head updating to the latest insert call, with a next pointing to the previous head?
def test_insert_points_to_next():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)

    current = my_list.head
    actual = current.value
    expected = 2
    assert actual == expected


# ? does the "includes" method accurately respond true for items inserted first (at the end of the list?)
def test_includes_accurate_hit_start():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(1)
    expected = True
    assert actual == expected


# ? does the "includes" method accurately respond true for items inserted somewhere in the middle?
def test_includes_accurate_hit_mid():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(2)
    expected = True
    assert actual == expected


# ? does the "includes" method accurately respond true for items inserted last?
def test_includes_accurate_hit_end():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(3)
    expected = True
    assert actual == expected


# ? does the "includes" method accurately respond false for values not present?
def test_includes_accurate_miss():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(3235)
    expected = False
    assert actual == expected


# ?Test below passed mid development. not sure how to healthily keep this test implemented without damaging the purpose of to_string, as this is a test of the middle step of to_string's function.
# def test_to_string_captures_values():
#     my_list = LinkedList()
#     my_list.insert(1)
#     my_list.insert(2)
#     my_list.insert(3)

#     actual = my_list.to_string()
#     expected = [3, 2, 1]
#     assert actual == expected


# ? Does to_string return a string value matching the required formatting?
def test_to_string():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.to_string()
    expected = "{ 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected


# ? Does the Append actually add a new node with the right value to the end of the list?
def test_appends_node():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    actual = my_list.to_string()
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"
    assert actual == expected


# ? does the insert_before method add a new node with a given value prior to an instance of the given existing number?
def test_insert_before_node():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    my_list.insert_before(2, 500)
    actual = my_list.to_string()
    expected = "{ 1 } -> { 500 } -> { 2 } -> { 3 } -> { 4 } -> NULL"
    assert actual == expected


# ? does the insert_after method add a new node with a given value directly after an instance of the given existing number?
def test_insert_after_node():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    my_list.insert_after(2, 500)
    actual = my_list.to_string()
    expected = "{ 1 } -> { 2 } -> { 500 } -> { 3 } -> { 4 } -> NULL"
    assert actual == expected


# ? does the insert_after method add a new node with a given value directly after the FIRST instance of the given existing number when there are duplicates?
def test_insert_after_node_dupes():
    my_list = LinkedList()
    my_list.insert(2)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(2)
    my_list.insert_after(2, 500)
    actual = my_list.to_string()
    expected = "{ 1 } -> { 2 } -> { 500 } -> { 2 } -> { 2 } -> NULL"
    assert actual == expected


# ? Can we append multiple times in a row?
def test_serial_append():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    my_list.append(4)
    my_list.append(5)
    my_list.append(4)
    actual = my_list.to_string()
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 4 } -> { 5 } -> { 4 } -> NULL"
    assert actual == expected


# ? does the insert_before method still work if the number we provide is the current head? (Why didn't you just use insert :T )
def test_insert_before_first():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    my_list.insert_before(1, 500)
    actual = my_list.to_string()
    expected = "{ 500 } -> { 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"
    assert actual == expected


# ? Does the insert_after method still work if the number we provide is the current end? (Why didn't you just use append :T )
def test_insert_after_end():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    my_list.insert_after(4, 500)
    actual = my_list.to_string()
    expected = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 500 } -> NULL"
    assert actual == expected


# ? Does providing a value for k that is bigger than the total node count of the linked list correctly return an "Exception" message?
def test_k_too_big():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    actual = my_list.kthFromEnd(57235)
    expected = "Exception"
    assert actual == expected


# ? Does providing a value for k that is negative correctly return an "Exception" message?
def test_k_negative():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    actual = my_list.kthFromEnd(-5)
    expected = "Exception"
    assert actual == expected


# ? Does providing 0 as a value for k return the last node's value?
def test_k_zero():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    actual = my_list.kthFromEnd(0)
    expected = 4
    assert actual == expected


# ? does providing 0 as a value of k work, while the linked list has only one node?
def test_k_zero_single_node():
    my_list = LinkedList()
    my_list.insert(1)
    actual = my_list.kthFromEnd(0)
    expected = 1
    assert actual == expected


# ? Does providing a k value that matches the node count of the linked list provide the first node? (note that this puts us one node past the head, so it should result in an exception!)
def test_k_length_matching():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    actual = my_list.kthFromEnd(4)
    expected = "Exception"
    assert actual == expected


# ? Basic usecase test. k refers to a node somewhere in the middle of the linked list
def test_k_happy_path():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    my_list.append(4)
    actual = my_list.kthFromEnd(2)
    expected = 2
    assert actual == expected


# TODO:


# !Where k is greater than the length of the linked list
# !Where k and the length of the list are the same
# !Where k is not a positive integer
# !Where the linked list is of a size 1
# !“Happy Path” where k is not at the end, but somewhere in the middle of the linked list


# !Write tests to prove the following functionality:

# !Can successfully add a node to the end of the linked list

# !Can successfully add multiple nodes to the end of a linked list

# !Can successfully insert a node before a node located i the middle of a linked list

# !Can successfully insert a node before the first node of a linked list

# !Can successfully insert after a node in the middle of the linked list

# !Can successfully insert a node after the last node of the linked list


#!     Can successfully instantiate an empty linked list
#!     Can properly insert into the linked list
#!     The head property will properly point to the first node in the linked list
#!     Can properly insert multiple nodes into the linked list
#!     Will return true when finding a value within the linked list that exists
#!     Will return false when searching for a value in the linked list that does not exist
#!     Can properly return a collection of all the values that exist in the linked list
