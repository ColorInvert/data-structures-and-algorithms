# Stack And Queue
<!-- Description of the challenge -->
"Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue"

With this being a linked list as the underlying data structure, the linked list requires a node system with a head, value, and next.
The feature requirements of the actual stack class are as follows:

- Must have default empty value for it's `top` value when initialized.
- Must have a `push` method that takes a value and adds a new node with the input value to the `top` of the stack.
- Must have a `pop` method that takes no args and both returns the value of, and removes from the stack the topmost node. Must raise bespoke exception when stack contains no more nodes.
- Must have `peek`, a method with no args that looks at the top node of the stack and returns the value within. Must raise bespoke exception when stack contains no more nodes.
- Must have a `is empty` method that returns a boolean stating whether the stack is empty.

In addition, using similar principles, create a queue.

Largely same requirements as the stack above, but instead of `top` it is `front`, instead of `push` it has `enqueue` which puts items at the back of the queue instead of front, has `dequeue` which functions exactly like `pop`, while `peek` and `is empty` function exactly the same.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Whiteboard Image](./WhiteBoard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
My approaches for a node-based stack and queue are (at least intended) to be of standard design, although it is my first time working through making these data structures. The big O Time performance for the push/enqueue functions are both (I hope) O(1) as required by the assignment.


## Solution
<!-- Show how to run your code, and examples of it in action -->
Code is available in queue.py and stack.py located in the data structures folder, and proof of their function can be verified through pytest. The relevant tests are in python/tests/test_queue.py and test_stack.py.
