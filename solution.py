def bracket_matcher(input):
  stack = []
  for letter in input:
    if letter in ['[', '{', '(']:
      stack.append(letter)
    elif letter in [']', '}', ')']:
      if len(stack) == 0:
        return False
      char = stack.pop()
      if letter == ']' and char != '[':
        return False
      if letter == '}' and char != '{':
        return False
      if letter == ')' and char != '(':
        return False
  return len(stack) == 0

print(bracket_matcher('abc(123)'))
# returns true

print(bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns true

print(bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print(bracket_matcher('()'))
# returns true

print(bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched