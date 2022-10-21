anInput = 'abc(123)'

anotherInput = '[]]'

lastTest = '[[]'

actuallyLastTest = 'abc123yay'

def bracket_matcher(input):
  testArr = []
  for i in range(len(input)):
    if input[i] == '[' or input[i] == '{' or input[i] == '(' or input[i] == ')' or input[i] == '}' or input[i] == ']':
      testArr.append(input[i])

  print(testArr)
  for j in range(len(testArr)):
    if j < len(testArr) - 1 and testArr[j] == '{' and testArr[j + 1] == '}':
      testArr.pop(j)
      testArr.pop(j)
    if j < len(testArr) - 1 and testArr[j] == '[' and testArr[j + 1] == ']': 
      testArr.pop(j)
      testArr.pop(j)
    if j < len(testArr) - 1 and testArr[j] == '(' and testArr[j + 1] == ')':
      testArr.pop(j)
      testArr.pop(j)

  print(testArr)
  print(True) if testArr == [] else print(False)

# bracket_matcher('abc(123)')
# # returns true

# bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

bracket_matcher('a[bc(123)]')
# returns true

# bracket_matcher('a[bc(12]3)')
# # returns false -- improperly nested

# bracket_matcher('a{b}{c(1[2]3)}')
# # returns true

# bracket_matcher('a{b}{c(1}[2]3)')
# # returns false -- improperly nested

# bracket_matcher('()')
# # returns true

# bracket_matcher('[]]')
# # returns false - no opening bracket to correspond with last character

# bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched
