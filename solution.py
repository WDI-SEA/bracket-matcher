def bracket_matcher(input):
  testArr = []
  for i in range(len(input)):
    if input[i] == '[' or input[i] == '{' or input[i] == '(':
      testArr.append(input[i])
    if input[i] == ']' or input[i] == '}' or input[i] == ')':
      if len(testArr) > 0:
        j = testArr.pop()
        if input[i] == ']' and j != '[' or input[i] == '}' and j != '{' or input[i] == ')' and j != '(':
          print(False)
          return
      else:
        print(False)
        return
  if testArr == []:
    print(True)
    return
  else:
    print(False)
    return
  

bracket_matcher('abc(123)')
# returns true

bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

bracket_matcher('a[bc(123)]')
# returns true

bracket_matcher('a[bc(12]3)')
# returns false -- improperly nested

bracket_matcher('a{b}{c(1[2]3)}')
# returns true

bracket_matcher('a{b}{c(1}[2]3)')
# returns false -- improperly nested

bracket_matcher('()')
# returns true

bracket_matcher('[]]')
# returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched
