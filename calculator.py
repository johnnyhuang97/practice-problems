from collections import defaultdict

def calculatorwithvariables(exp, var):
  if exp == None or len(exp) == 0:
    return 0
  
  unknwn = defaultdict(int)
  stack = []
  num = 0
  sign = 1

  for i in range(len(exp)):
    curr = exp[i]
    if curr == '+':
      sign = 1
    elif curr == '-':
      sign = -1
    elif curr.isdigit():
      dig = int(curr)
      while i+1 < len(exp) and exp[i+1].isdigit():
        dig *= 10
        dig += exp[i+1]
        i += 1
      num+= dig*sign
    elif curr == '(':
      stack.append(num)
      stack.append(sign)
      num = 0
      sign = 1
    elif curr == ')':
      num = num*stack.pop() + stack.pop()
    elif curr.isalpha():
      #print(curr)
      if str(curr) in var:
        num+=sign*var[curr]
      else:
        temp = sign
        if len(stack) == 0:
          unknwn[curr] += sign
        else:
          unknwn[curr] += (sign*stack[-1])
  
  res = str(num)
  print(unknwn)
  for v in unknwn:
    if unknwn[v] < 0:
      res += "{}{}".format(str(unknwn[v]),str(v))
    elif unknwn[v] > 0:
      res += "{}{}{}".format("+", str(unknwn[v]), str(v))
  return res

expression = "(a+b)+c+d+1+d-(d-d-d+1)"
variables = {"a":1,"b":2,"c":3} 
print(calculatorwithvariables(expression, variables))