from Stack import Stack

def bracket_matcher(input):
  bracket_stack = Stack()
  open_brackets = ['{', '(', "["]
  close_brackets = ['}', ")", "]"]
  for i in range(len(input)):
    if input[i] in open_brackets:
      bracket_stack.push(input[i])
    elif input[i] in close_brackets:
      index = close_brackets.index(input[i])
      if open_brackets[index] == bracket_stack.peek():
        bracket_stack.pop()
      else:
        return False
  if bracket_stack.isEmpty():
    return True
  else:
    return False

# True
print(bracket_matcher('abc(123)'))

# False
print(bracket_matcher('a[b]c(123'))

# True
print(bracket_matcher('a[bc(123)]'))

# False
print(bracket_matcher('a[bc(12]3)'))

# True
print (bracket_matcher('a{b}{c(1[2]3)}'))

# False
print (bracket_matcher('a{b}{c(1}[2]3)'))

# True
print (bracket_matcher("()"))

# False
print (bracket_matcher('[]]'))

# True
print(bracket_matcher("abc123yay"))