

def bracket_matcher(input): 
    openBracket = ["{", "[","("] 
    closeBracket = ["}","]",")"] 

    stack = [] 
    for i in input: 
      #As an open bracket is encountered in a function, it is appended to the stack list
        if i in openBracket: 
            stack.append(i) 
      #As a closed bracket is encountered pop it
        elif i in closeBracket: 
            l = closeBracket.index(i) 
            if ((len(stack) > 0) and
                #if index bracket type at position of open bracket equals whats at that index in stack list then pop
                (openBracket[l] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
      # If zero then balanced/true
    if len(stack) == 0: 
        return True
  


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