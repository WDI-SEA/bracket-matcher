from collections import deque 

def bracket_matcher(input): 
    stack = deque() 
    opening= ['{','(','[']
    closing = ['}',')',']']

    for each in input:
        if each in opening:
              stack.append(each)
        elif each in closing:
            if(len(stack)!=0):
                  index = closing.index(each)
                  ele = stack[len(stack)-1]
                  if(ele == opening[index]):
                      stack.pop()
            elif (len(stack)== 0):         
                       return False 
         
    
    if len(stack)== 0:
        return True
    return False            


# bracket_matcher : other variation
def test_brackets(input):
    opens = {'{': '}', '(': ')', '[': ']'}
    closes = {'}': '{', ')': '(', ']': '['}
    stack = []
    for c in input:
        if c in opens: stack.append(c)
        elif c in closes:
            if not stack: return False
            if not opens[stack.pop()] == c: return False
    return not len(stack)




status = bracket_matcher('{ac}}e{{hs}')
print('status',status)

status1 = bracket_matcher('a{()}}')
print('status',status1)

status2 = bracket_matcher('{ac}e{{hs}')
print('status',status2)

print('abc(123)',bracket_matcher('abc(123)'))
# returns true

print('a[b]c(123',bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print('a[bc(123)]',bracket_matcher('a[bc(123)]'))
# returns true

print('a[bc(12]3)',bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print('a{b}{c(1[2]3)}',bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print('a{b}{c(1}[2]3)',bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print('()',bracket_matcher('()'))
# returns true

print('[]]',bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print('abc123yay',bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched