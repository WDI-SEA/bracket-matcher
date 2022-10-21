from collections import deque
def bracket_matcher(input):
  
  stack = deque()
  bracket = ['[','{','(']
  close = {
    ']':'[',
    '}':'{',
    ')':'('}
  for value in input:
    if(value in close):
      if(len(stack)==0):
        return False
      if(close[value] != stack.pop()): 
        return False
    elif(value in bracket):
      stack.append(value)

  if(len(stack)!=0):
    return False
  return True
    

      

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
