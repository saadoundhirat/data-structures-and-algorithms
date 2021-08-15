# **Lab & code challenge 15 Trees**

# Trees
<!-- Short summary or background information -->
- A tree is a nonlinear data structure, compared to arrays, linked lists, stacks and queues which are linear data structures. A tree can be empty with no nodes or a tree is a structure consisting of one node called the root and zero or one or more subtrees.

## Challenge
<!-- Description of the challenge -->
- making tree data structure and make Tree nodes then make another class called binary search tree that inherits from the binary tree class
- binary search tree contains to methods a- add b- contains

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Add
  - Arguments: value
  - Return: nothing
  - Adds a new node with that value in the correct location in the binary search tree.
- Contains
  - Argument: value
  - Returns: boolean indicating whether or not the value is in the tree at least once.

## API
<!-- Description of each method publicly available in each of your trees -->
- Add time complexity: O(log n) cuz we add with binary search tree.
- Contains time complexity: O(log n) cuz we are doing a binary search tree

# **Check List:**

- [x] Top-level README “Table of Contents” is updated
- [x] README for this challenge is complete
- [x] Summary, Description, Approach & Efficiency, Solution
- [x] Picture of whiteboard
- [x] Link to code
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
