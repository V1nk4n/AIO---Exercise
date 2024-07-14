
class MyStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0]*capacity
        self.top_pointer = -1

    def is_empty(self):
        if self.top_pointer == -1:
            return True
        return False

    def is_full(self):
        if self.top_pointer == self.capacity - 1:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return
        pop_res = self.stack[self.top_pointer]
        self.top_pointer -= 1
        return pop_res

    def push(self, value):
        if self.is_full():
            return
        self.top_pointer += 1
        self.stack[self.top_pointer] = value

    def top(self):
        if self.is_empty():
            return
        top_res = self.stack[self.top_pointer]
        return top_res


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
