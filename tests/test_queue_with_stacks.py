from data_structures_and_algorithms_python.data_structures.stacks_and_queues.queue_with_stacks import PseudoQueue

import pytest


"""
Test Cases:
    1. Enqueue into the queue.
    2. Enqueue multiple values into the queue.
    3. Dequeue from the queue.
    4. Dequeue multiple values from the queue.
    5. Raise an exception when dequeuing from an empty queue.
"""

def test_stacks_enqueue():
    queue = PseudoQueue()
    queue.enqueue(7)
    assert queue.inStack.top.value == 7


def test_stacks_enqueue_multiple():
    queue = PseudoQueue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue(2)
    assert queue.inStack.top.value == 2
    assert queue.inStack.top.next.value == 3
    assert queue.inStack.top.next.next.value == 7

def test_stacks_dequeue():
    queue = PseudoQueue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.outStack.top.value == 3
    assert queue.outStack.top.next.value == 2
    assert queue.outStack.top.next.next == None

def test_stacks_dequeue_multiple():
    queue = PseudoQueue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.outStack.top.value == 2
    assert queue.outStack.top.next == None

def test_stacks_dequeue_empty():
    queue = PseudoQueue()
    with pytest.raises(AttributeError):
        assert queue.dequeue()



