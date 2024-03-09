class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)


# Example usage
queue = Queue()

# Enqueueing elements into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: 3
print("Queue peek:", queue.peek())  # Output: 1

# Dequeueing elements from the queue
print("Dequeued item:", queue.dequeue())  # Output: 1
print("Dequeued item:", queue.dequeue())  # Output: 2

print("Queue size:", queue.size())  # Output: 1
print("Queue peek:", queue.peek())  # Output: 3

# Dequeue the remaining item
print("Dequeued item:", queue.dequeue())  # Output: 3

# Trying to dequeue from an empty queue
print("Dequeued item:", queue.dequeue())  # Output: Queue is empty, None
