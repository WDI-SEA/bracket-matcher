# ## # ## # ## # ## #
# CLASS REVIEW

def bracket_matcher(input):
  # use a list to hold opening character to determine if a new pair has started
  # use a dictionary to establish the pairs
  # use an empty list variable to store the opening brackets for later comparisons

  # loop over all of input
  # if the current element is a bracket (check our list) then push the bracket to our stack variable for later comparisons

  # if the current element is a closing bracket (check our dictionary)
    # if the stack variable has no length, then the closing bracket current element will never have a match, so return False!
    # if the last element in the stack variable is exactly equal to the value associated with the key that is the current element, then return True!














# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

#   def __str__(self):
#     return self.data


# class Stack:
#   def __init__(self):
#     self.head = None


#   def __str__(self):
#     current_node = self.head
#     string = str(current_node)


#     while current_node.next:
#       string += f' -> {str(current_node.next)}'
#       current_node = current_node.next

#     return f' [ {string} ]'


#   def push(self, data):
#     if self.head == None:
#       self.head = Node(data)
#     else:
#       new_node = Node(data)
#       new_node.next = self.head
#       self.head = new_node


#   def pop(self):
#     if self.head == None:
#       return None
#     else:
#       pop_value = self.head.data
#       self.head = self.head.next
#       return pop_value

  
#   def peek(self):
#     if self.head == None:
#       return None
#     else:
#       return self.head.data

# my_stack = Stack()




# def bracket_matcher(input):
#   valid_chars = ''

#   table = []
#   object = { '(' : ')', '[' : ']', '{' : '}' }
#   for i in input:
#     if i in object.keys() or i in object.values():
#       valid_chars += i
#       print(valid_chars)
#   if len(valid_chars) != 0:
#     for i in valid_chars:
#       if i in object:
#         table.append(i)
#       else:
#         if table == []:
#           return False
#         j = table.pop()
#       # my_stack.push(i)

#   # print(my_stack)







input = input('Please enter a string with brackets, parenteses, or braces... \n > ')
bracket_matcher(input)
