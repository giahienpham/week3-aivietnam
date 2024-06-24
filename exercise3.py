class MyStack:
    def __init__(self, capacity):
      self.__capacity = capacity
      self.__stack = []
    def is_empty(self):
      return len(self.__stack)==0
    def is_full(self):
      return len(self.__stack) == self.__capacity
    def push(self, value):
      if not self.is_full():
        self.__stack.append(value)
      else:
        raise Exception("Stack is full")
    def pop(self):
      if not self.is_empty():
        return self.__stack.pop()
      else:
        raise Exception("Stack is empty")
    def top(self):
      if not self.is_empty():
        return self.__stack[-1]
      else:
        raise Exception("Stack is empty")
    def size(self):
      return len(self.__stack)
mystack = MyStack(3)
print(mystack.is_empty())
mystack.push(2)
mystack.is_empty()
mystack.push(9)
mystack.top()