class Queue:
    def __init__(self):
        self._head = Stack()
        self._tail = Stack()

    def enqueue(self, data):
        self._tail.push(data)

    def dequeue(self):
        if self._head:
            return self._head.pop()

        return self._tail_to_head().pop()

    def peek(self):
        if self._head:
            return self._head.top()

        return self._tail_to_head().top()

    def _tail_to_head(self):
        while self._tail:
            self._head.push(self._tail.pop())

        return self._head


class Stack:
    def __init__(self):
        self._l = []

    def push(self, data):
        self._l.append(data)

    def pop(self):
        return self._l.pop()

    def __len__(self):
        return len(self._l)

    def top(self):
        if self._l:
            return self._l[-1]
        return None