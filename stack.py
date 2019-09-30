class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(self.size() - 1)

    def peek(self):
        return self.stack[self.size() - 1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        output = ''
        for each in self.stack:
            output += each
        return output