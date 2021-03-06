"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value 
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      # self.tail.set_next(None)
    self.tail = new_node

  def remove_head(self):
    curr_head = self.head
    if self.head:
      self.head = self.head.get_next()
      self.tail = None
      return curr_head.value

  def contains(self, value):
    test_node = self.head
    # if self.head:
    while test_node:
      if test_node.get_value() == value:
        return True
      else:
        test_node = test_node.get_next()
    return False

  def get_max(self):
    if self.head is None:
      return None
    biggest = self.head.value
    current = self.head.get_next()
    while current:
      if current.value > biggest:
        biggest = current.value
      current = current.next_node
    return biggest
