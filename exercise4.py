class MyQueue:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__queue = []
  def is_empty(self):
    return len(self.__queue)==0
  def is_full(self):
    return len(self.__queue) == self.__capacity
  def enqueue(self, value):
    if self.is_full():
      raise Exception("Queue is full")
    else:
      self.__queue.append(value)
  def dequeue(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    else:
      return self.__queue.pop(0)
  def font(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    else:
      return self.__queue[0]
  def size(self):
    return len(self.__queue)

my_queue = MyQueue(3)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.dequeue()