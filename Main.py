import os
class Stack:
    def _init_(self, size):
        self.items = [None]*size
        self.size = size
        self.top = -1

    def is_empty(self):
        # Write code here
        return self.top == -1

    def is_full(self):
        # Write code here
        return self.top == (self.size-1)

    def push(self, data):
        if not self.is_full():
            # Write code here
            self.top += 1
            self.items[self.top] = data

    def pop(self):
        if not self.is_empty():
            # Write code here
            x = self.items[self.top]
            self.top -= 1

    def status(self):
        # Write code here
        for i in range(self.top+1):
            print(self.items[i])
