def evalRPN(tokens):
  stack = []
  for c in tokens:
    if c == '+':
      stack.append(stack.pop() + stack.pop())
    elif c == '*':
      stack.append(stack.pop() * stack.pop())
    elif c == '-':
      a, b = stack.pop(), stack.pop()
      stack.append(b - a)
    elif c == '/':
      a, b = stack.pop(), stack.pop()
      stack.append(int(b / a))
    else:
      stack.append(int(c))
  return stack[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))