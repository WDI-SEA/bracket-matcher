def bracket_matcher(input):

  openBrackets = {'(', '[', '{'}
  closBrackets = {')', ']', '}'}
  checkOpen = []
  checkClosed = []

  for i in input:
    if i in openBrackets:
      checkOpen.append(i)
    if i in closBrackets:
      if i == ')':
        checkClosed.insert(0, '(')
      elif i == ']':
        checkClosed.insert(0, '[')
      elif i == '}':
        checkClosed.insert(0, '{')
  # print(checkOpen)
  # print(checkClosed)

  if len(checkClosed) == 0 and len(checkOpen) == 0:
    return True
  if len(checkClosed) != len(checkOpen):
    return False

  for i in range(len(checkOpen)):
      if checkOpen[i] != checkClosed[i]:
        return False
      else:
        return True

# print(bracket_matcher('{(bxbxa)(bxbxb)}'))
# print(bracket_matcher('[dasdy(c)ddd  ] alkd }'))

# print(bracket_matcher('abc(123)'))
# returns true

# print(bracket_matcher('a[b]c(123'))
# # returns false -- missing closing parens

# print(bracket_matcher('a[bc(123)]'))
# # returns true

# print(bracket_matcher('a[bc(12]3)'))
# # returns false -- improperly nested

# print(bracket_matcher('a{b}{c(1[2]3)}'))
# # returns true

# print(bracket_matcher('a{b}{c(1}[2]3)'))
# # returns false -- improperly nested

# print(bracket_matcher('()'))
# # returns true

print(bracket_matcher('[]]'))
# # returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# # returns true -- no brackets = correctly matched