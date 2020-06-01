
  

def bracket_matcher(input): 
  open_list = ["[","{","("] 
  close_list = ["]","}",")"] 
  stack = [] 

  for i in input: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "false"
  if len(stack) == 0: 
        return "true"
  else: 
        return "false"



print(bracket_matcher("({[})")) 