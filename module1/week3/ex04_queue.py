"test"


class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0]*capacity
        self.front_pointer = -1
        self.rear_pointer = -1

    def is_empty(self):
        if self.rear_pointer == -1:
            return True
        return False

    def is_full(self):
        if self.rear_pointer == self.capacity - 1:
            return True
        return False

    def dequeue(self):
        if self.is_empty():
            return
        dequeue_res = self.queue[self.rear_pointer]
        self.rear_pointer -= 1
        return dequeue_res

    def enqueue(self, value):
        if self.is_full():
            return
        for i in range(self.rear_pointer+1):
            self.queue[i+1] = self.queue[i]
        self.rear_pointer += 1
        self.queue[0] = value

    def front(self):
        return self.queue[self.rear_pointer]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
