from stack import Stack 

def bracket_matcher(input):
  stack = Stack()
  leftBrackets = ['[','{','(']
  rightBrackets = [']','}',')']
  for char in input:
    if char in leftBrackets:
      stack.push(char)
    elif char in rightBrackets:
      leftBrack = stack.pop()
      if char is ']' and leftBrack is '[':
        continue
      elif char is '}' and leftBrack is '{':
        continue
      elif char is ')' and leftBrack is '(':
        continue
      else:
        return False
    else:
      continue
  return True
