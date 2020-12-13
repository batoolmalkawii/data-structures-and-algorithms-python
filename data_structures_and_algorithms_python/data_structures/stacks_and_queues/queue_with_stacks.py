#from stacks_and_queues import Stack, Node
from data_structures_and_algorithms_python.data_structures.stacks_and_queues.stacks_and_queues import Stack, Node

class PseudoQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, value):
        self.inStack.push(value)

    def dequeue(self):
        if (self.inStack.top == None and self.outStack.top == None):
            raise AttributeError("Queue is empty.")
        if (self.outStack.top == None):
            while(self.inStack.top):
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()



if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(0)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

