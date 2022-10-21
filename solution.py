def bracket_matcher(input):
  open = ['[','(','{']
  close = [']',')','}']
  stack = []

  for i in range(len(input)):
    if input[i] in close and len(stack) == 0:
      return False
    elif input[i] in open:
      stack.append(input[i])
    elif input[i] in close:
      idx = close.index(input[i])
      if open[idx] == stack[len(stack) - 1]:
        stack.pop()
      else:
        print(stack)
        return False
      if len(stack) > 0:
        print(stack)
        return False
      return True

print('number 1:', bracket_matcher('abc(123)'))
# returns true

print('number 2: ', bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print('number 3:', bracket_matcher('a[bc(123)]'))
# returns true

print('number 4:', bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print('number 5:', bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print('number 6:', bracket_matcher("a{b}{c(1}[2]3)"))
# returns false -- improperly nested

print('number 7:', bracket_matcher('()'))
# # returns true

print('number 8:', bracket_matcher('[]]'))
# # returns false - no opening bracket to correspond with last character

print('number 9:', bracket_matcher('abc123yay'))
# # returns true -- no brackets = correctly matched