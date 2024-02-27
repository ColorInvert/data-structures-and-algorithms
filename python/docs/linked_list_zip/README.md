# Linked List Zip
<!-- Description of the challenge -->
Extend the previously created linked_list.py to have a new method called ```zipLists(list1, list2)``` which converts the two linked list into a single linked list, with the nodes alternating back and forth between list 1 and 2 (list1 index0, list2 index0, list1 index1, list2 index1...)

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Whiteboard Image](./WhiteBoard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Bit of a disaster this one. The approach I was taking, and the one I whiteboarded out before coding was messy, and fundamentally flawed in a couple of ways. Ultimately, I had to scrap my code when I realized it wasn't working, and through research found the much more elegant solution of just... Append to a new list the values of the 2 lists, back and forth. Append from list1, append from list2. That's it. Ugh.

## Solution
<!-- Show how to run your code, and examples of it in action -->

Code can be ran via `python linked_list.py`
which will do the following

```
    # Testing for ziplist. Make 2 linked lists, see if the output of ziplists
    # performed while taking both as variables gives expected output.
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.insert(20)
    print(ll.includes(10))

    ll_2 = LinkedList()
    ll_2.insert(2)
    ll_2.insert(4)
    ll_2.insert(6)
    ll_2.insert(8)

    zipped = LinkedList.zipLists(ll, ll_2)
    print(f"linked list address is {zipped}")

    print(f"And the value is {zipped.to_string()}")
```
And resulting in
```
True
linked list address is <__main__.LinkedList object at 0x7f0d2ad99010>
And the value is { 20 } -> { 8 } -> { 15 } -> { 6 } -> { 10 } -> { 4 } -> { 5 } -> { 2 } -> NULL
```
proving function.
