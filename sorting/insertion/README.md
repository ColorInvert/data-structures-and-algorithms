# Blog Notes: Insertion Sort
[original google doc with illustrations can be viewed here.](https://docs.google.com/document/d/1valkQYVeUg3b3k2bwh6DJ8JnB2ZNm7azicWTesKi1OQ/edit?usp=sharing)

Raw text version without inline illustrations below:

## Insertion sort, a breakdown of the exact mechanics

### The pseudocode
```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```


We have two functions defined, the first being the nested function of the second.

The deeper function is Insert() and takes the following variables: an integer list called 'sorted', and a int value.

the outer function is called InsertionSort and takes an input list of integers.

As Insert is the inner function, we start with InsertionSort, called with our input list of integers.

First, a new empty array called 'sorted' is created.

then, the index 0 value of sorted is set to be the index 0 value of the input list.

From here, we enter a for loop that performs it's action repeatedly, once per index of the input list.

Inside the for loop, Insert() is called with the argument of our 'sorted' list, and the value of the current index of the input list, as defined by what iteration of the for loop we are on, however since we have already directly copied the first index item from the input list over to 'sorted', we start from index[1] not index[0].

Now that we are inside the nested function Insert(), we have received two input arguments,
a 'sorted' list containing only the first value from our input list at its first index, and input list's index[1].

a new variable is declared, i, which is set to 0.

A while loop begins, that goes until the input value of input[1] is greater than the value of 'sorted' at index [i].


If a yes response from the while loop indicating a repeat, a single line is called within this while loop, which increments i by 1. By running a while loop with i incrementing by one each time, value is compared to each element in "sorted" in index order, until the moment that value is greater than the item in the index.

with the value of i still marking the point in which value is higher than the value in the "sorted" list, begin a new while loop.

This while loop repeats for as long as i is less than the total number of entries in the "sorted" list.

a new variable is declared called temp, and it is set to the value at "sorted"[i], which was established already as being the first index in which our value is greater than.

the value for "sorted"[i] is then changed to be value.

value is set to be equal to temp.

I is then incremented by 1, and the while loop if condition still met.


When the loop is broken, value, which is now equal to temp, is now appended to the end of the "sorted" list.

With this, the inner Insert() function is completed, and we go up one level. the i value of InsertionSort() is incremented by one, and Insert() is called again, with the newly appended to "sorted" list, and the value of the input list at the next index.

This cycle repeats, until the point in which InsertionSort()'s i value has reached the end of the input list's indices. With this for loop broken, "sorted" has been appended to enough times that it now matches the item count, and contents, of the input list, but sorted into numerical order.

InsertionSort() then returns "sorted", our now fully sorted version of the input list.



The raw code for a python version of this is as follows (note that it needed to be modified in its checks for end of index due to potential for index out of range errors):

```
reverse = [20, 18, 12, 8, 5, -2]
sames = [5, 12, 7, 5, 5, 7]
almost = [2, 3, 5, 7, 13, 11]




def Insert(sorted, value):
    i = 0
    while i <len(sorted) and value > sorted[i]:
        i = i + 1
    if i == len(sorted):
        sorted.append(value)
    else:
        while i < len(sorted):
            temp = sorted[i]
            sorted[i] = value
            value = temp
            i = i + 1
        sorted.append(value)




def InsertionSort(input):
    sorted = []
    sorted.append(input[0])
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted




print(f"reverse input gives us {InsertionSort(reverse)}")
print(f"sames input gives us {InsertionSort(sames)}")
print(f"almost input gives us {InsertionSort(almost)}")
```

This code serves as both a test and as a duplication of the pseudocode. The three provided examples of test cases are provided, and the print statements at the end perform the sort on them, and give back the expected results.
