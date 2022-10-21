open_list = ["[","{","("]
close_list = ["]","}",")"]


def bracket_matcher(input):
	stack = []
	for i in input:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			position = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[position] == stack[len(stack)-1])):
				stack.pop()
			else:
				return False
	if len(stack) == 0:
		return True
	else:
		return False


print(bracket_matcher('abc(123)'))
print(bracket_matcher('a[b]c(123'))
print(bracket_matcher('a[bc(123)]'))
print(bracket_matcher('a[bc(12]3)'))
print(bracket_matcher('a{b}{c(1[2]3)}'))
print(bracket_matcher('a{b}{c(1}[2]3)'))
print(bracket_matcher('()'))
print(bracket_matcher('[]]'))
print(bracket_matcher('abc123yay'))
