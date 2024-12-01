import sys
from yogi import scan

class EmptyContainerError(Exception):
    """Error when attempting to access an element from an empty container."""
    pass


class QueueArray:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10  # Moderate capacity for new queues

    def __init__(self):
        """Create an empty queue."""
        self._storage = [None] * QueueArray.DEFAULT_CAPACITY
        self._count = 0
        self._front_index = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._count

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._count == 0

    def peek(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise EmptyContainerError if the queue is empty.
        """
        if self.is_empty():
            raise EmptyContainerError('Queue is empty')
        return self._storage[self._front_index]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise EmptyContainerError if the queue is empty.
        """
        if self.is_empty():
            raise EmptyContainerError('Queue is empty')
        item = self._storage[self._front_index]
        self._storage[self._front_index] = None  # help garbage collection
        self._front_index = (self._front_index + 1) % len(self._storage)
        self._count -= 1
        if 0 < self._count < len(self._storage) // 4:
            prev_size = sys.getsizeof(self._storage)
            self._resize(len(self._storage) // 2)
            curr_size = sys.getsizeof(self._storage)
            QueueArray._resize_check(prev_size, curr_size)
        return item

    def enqueue(self, item):
        """Add an element to the back of the queue."""
        if self._count == len(self._storage):
            prev_size = sys.getsizeof(self._storage)
            self._resize(2 * len(self._storage))  # double the array size
            curr_size = sys.getsizeof(self._storage)
            QueueArray._resize_check(prev_size, curr_size)
        available_index = (self._front_index + self._count) % len(self._storage)
        self._storage[available_index] = item
        self._count += 1

    def _resize(self, new_capacity):
        """Resize to a new list of capacity >= len(self)."""
        old_storage = self._storage
        self._storage = [None] * new_capacity
        current_index = self._front_index
        for i in range(self._count):
            self._storage[i] = old_storage[current_index]
            current_index = (current_index + 1) % len(old_storage)
        self._front_index = 0

    @staticmethod
    def _resize_check(prev_size, curr_size):
        if prev_size != curr_size:
            print(f'resized from {prev_size} to {curr_size}')


class DoubleEndedQueue(QueueArray):
    """Deque (Double-Ended Queue) Abstract Data Type using QueueArray"""

    def add_to_front(self, item):
        """Add an element at the front of the deque."""
        if self._count == len(self._storage):
            prev_size = sys.getsizeof(self._storage)
            self._resize(2 * len(self._storage))  # double the array size
            curr_size = sys.getsizeof(self._storage)
            QueueArray._resize_check(prev_size, curr_size)

        self._front_index = (self._front_index - 1) % len(self._storage)
        self._storage[self._front_index] = item
        self._count += 1

    def add_to_back(self, item):
        """Add an element at the back of the deque (same as enqueue)."""
        self.enqueue(item)

    def remove_from_front(self):
        """Remove the first element of the deque and return its value."""
        if self.is_empty():
            raise EmptyContainerError('Deque is empty')
        return self.dequeue()

    def remove_from_back(self):
        """Remove the last element of the deque and return its value."""
        if self.is_empty():
            raise EmptyContainerError('Deque is empty')

        last_index = (self._front_index + self._count - 1) % len(self._storage)
        item = self._storage[last_index]
        self._storage[last_index] = None
        self._count -= 1

        if 0 < self._count < len(self._storage) // 4:
            prev_size = sys.getsizeof(self._storage)
            self._resize(len(self._storage) // 2)
            curr_size = sys.getsizeof(self._storage)
            QueueArray._resize_check(prev_size, curr_size)

        return item

    def peek_last(self):
        """Return the last element of the deque without modifying it."""
        if self.is_empty():
            raise EmptyContainerError('Deque is empty')

        last_index = (self._front_index + self._count - 1) % len(self._storage)
        return self._storage[last_index]


if __name__ == '__main__':
    n = scan(int)
    while n is not None:
        deque_instance = DoubleEndedQueue()

        print(f'len {len(deque_instance)}')
        if deque_instance.is_empty():
            print('deque empty')

        for i in range(n // 2):
            deque_instance.add_to_front(i)
            print(f'{i} added to the front')

        for i in range(n // 2, n):
            deque_instance.add_to_back(i)
            print(f'{i} added to the back')

        print(f'len {len(deque_instance)}')
        try:
            print(f'first {deque_instance.peek()}')
        except:
            print('first error: deque empty')

        try:
            print(f'last {deque_instance.peek_last()}')
        except:
            print('last error: deque empty')

        for _ in range(n // 2):
            try:
                item = deque_instance.remove_from_back()
                print(f'{item} deleted from the back')
            except EmptyContainerError:
                print('delete last error: deque empty')

        print(f'len {len(deque_instance)}')
        try:
            print(f'first {deque_instance.peek()}')
        except:
            print('first error: deque empty')

        try:
            print(f'last {deque_instance.peek_last()}')
        except:
            print('last error: deque empty')

        for _ in range(n // 2 + 1):
            try:
                item = deque_instance.remove_from_front()
                print(f'{item} deleted from the front')
            except EmptyContainerError:
                print('delete first error: deque empty')

        try:
            item = deque_instance.remove_from_back()
            print(f'{item} deleted from the back')
        except EmptyContainerError:
            print('delete last error: deque empty')

        print(f'len {len(deque_instance)}')
        try:
            print(f'first {deque_instance.peek()}')
        except EmptyContainerError:
            print('first error: deque empty')

        try:
            print(f'last {deque_instance.peek_last()}')
        except:
            print('last error: deque empty')

        print()

        n = scan(int)
