def bracket_matcher(input):
  brackets_start = ['[','(','{']
  brackets_end = [']',')','}']
  stack_list = []
  for i in range(len(input)):
    if input[i] in brackets_end and len(stack_list) == 0:
      return False
    elif input[i] in brackets_start:
      stack_list.append(input[i])
    elif input[i] in brackets_end:
      idx = brackets_end.index(input[i])
      if brackets_start[idx] == stack_list[len(stack_list)-1]:
        stack_list.pop()
      else:
        print(stack_list)
        return False
  if len(stack_list) > 0:
    print(stack_list)
    return False
  return True

print(bracket_matcher('a[b{c(1[2]3)}]'))