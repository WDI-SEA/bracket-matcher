# def bracket_matcher(input):
#   open = ['[','(','{']
#   close = [']',')','}']
#   stack = []

#   for i in range(len(input)):
#     if input[i] in close and len(stack) == 0:
#       return False
#     elif input[i] in open:
#       stack.append(input[i])
#     elif input[i] in close:
#       idx = close.index(input[i])
#       if open[idx] == stack[len(stack) - 1]:
#         stack.pop()
#       else:
#         print(stack)
#         return False
#       if len(stack) > 0:
#         print(stack)
#         return False
#       return True

# print('number 1:', bracket_matcher('abc(123)'))
# # returns true

# print('number 2: ', bracket_matcher('a[b]c(123'))
# # returns false -- missing closing parens

# print('number 3:', bracket_matcher('a[bc(123)]'))
# # returns true

# print('number 4:', bracket_matcher('a[bc(12]3)'))
# # returns false -- improperly nested

# print('number 5:', bracket_matcher('a{b}{c(1[2]3)}'))
# # returns true

# print('number 6:', bracket_matcher("a{b}{c(1}[2]3)"))
# # returns false -- improperly nested

# print('number 7:', bracket_matcher('()'))
# # # returns true

# print('number 8:', bracket_matcher('[]]'))
# # # returns false - no opening bracket to correspond with last character

# print('number 9:', bracket_matcher('abc123yay'))
# # # returns true -- no brackets = correctly matched


###APRIL SOLVE###

def bracket_matcher(input):
    # use a list to hold opening character to determine if a new pair has started
	open = ['[','(','{']	
	# use a dictionary to establish the pairs
	close = {
		']':'[',
		')':'(',
		'}':'{'
	}
    # use a empty list variable to store the opening brackets for later comparison
	stack = []
    # loop over all of input
	for bracket in input:
		# print("BRACKET\n", bracket)
    	# if the current element is a bracket(check our list) then
		if bracket in open:
			# push the bracket to the stack for later comparisons
			stack.append(bracket)
			# print("STACK\n", stack)
   		#  if the current element is a closing bracket (check our dictionary) then
		if bracket in close:
    		#  - if the stack variable has no length, then the closing bracket current  element will never have a match, so return false
			if len(stack) < 1:
				return False
			# - if the last element in the stack is equal to the the current element, then pop from stack so doesn't confuse future comparisons
			# print('STACK\n', stack)
			# print('DICTIONARY\n', close[bracket])
			if close[bracket] == stack[len(stack) - 1]:
				stack.pop()
	# if stack variable has a length after the loop is finished, then one bracket didnt' have a pair so return false
	if len(stack) > 0:
		return False
	# if we made it this far, we should be good. return true.
	return True


print('number 1:', bracket_matcher('abc(123)'))
# # returns true

print('number 2:', bracket_matcher('a[b]c(123'))
# # returns false -- missing closing parens

print('number 3:', bracket_matcher('a[bc(123)]'))
# # returns true

print('number 4:', bracket_matcher('a[bc(12]3)'))
# # returns false -- improperly nested

print('number 5:', bracket_matcher('a{b}{c(1[2]3)}'))
# # returns true

print('number 6:', bracket_matcher("a{b}{c(1}[2]3)"))
# # returns false -- improperly nested

print('number 7:', bracket_matcher('()'))
# # # returns true

print('number 8:', bracket_matcher('[]]'))
# # # returns false - no opening bracket to correspond with last character

print('number 9:', bracket_matcher('abc123yay'))
# # # returns true -- no brackets = correctly matched