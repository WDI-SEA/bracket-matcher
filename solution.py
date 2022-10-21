class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

  def __str__(self):
    return self.data


class Stack:
  def __init__(self):
    self.head = None


  def __str__(self):
    current_node = self.head
    string = str(current_node)


    while current_node.next:
      string += f' -> {str(current_node.next)}'
      current_node = current_node.next

    return f' [ {string} ]'


  def push(self, data):
    if self.head == None:
      self.head = Node(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node


  def pop(self):
    if self.head == None:
      return None
    else:
      pop_value = self.head.data
      self.head = self.head.next
      return pop_value

  
  def peek(self):
    if self.head == None:
      return None
    else:
      return self.head.data

my_stack = Stack()




def bracket_matcher(input):
  table = []
  open = ['[', '{', '(']
  close = [']', '}', ')']
  for i in input:
    if i in open or i in close:
      print(i)
      table += i
  print(table)


input = input('Please enter a string with brackets, parenteses, or braces... \n > ')
bracket_matcher(input)
