########################
#test code challenge 10#
########################
import pytest
from stack_and_queue.stack_and_queue import Stack,Queue,Node,Stack_empty,Queue_empty
# Can successfully push onto a stack
def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.top.data== 1

# Can successfully push multiple values onto a stack
def test_stack_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.data == 3
# Can successfully pop off the stack
def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
# Can successfully empty a stack after multiple pops
def test_stack_pop_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
# Can successfully peek the next item on the stack
def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2

# Can successfully instantiate an empty stack
def test_stack_empty():
    stack = Stack()
    assert stack.is_empty() == True
# # Calling pop or peek on empty stack raises exception
# def test_stack_empty_pop_peek():
#     with pytest.raises(Stack_empty):
#         stack = Stack()
#         stack.pop()
        
# Can successfully enqueue into a queue
def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.data == 1
# Can successfully enqueue multiple values into a queue
def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front.data == 1

# Can successfully dequeue out of a queue the expected value
def dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
# Can successfully peek into a queue, seeing the expected value
def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1
# Can successfully empty a queue after multiple dequeues
def test_queue_dequeue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

# Can successfully instantiate an empty queue
def test_queue_empty():
    queue = Queue()
    assert queue.is_empty() == True

# # Calling dequeue or peek on empty queue raises exception
# def test_queue_empty_dequeue_peek():
#     with pytest.raises(Queue_empty):
#         queue = Queue()
#         queue.dequeue()
        
