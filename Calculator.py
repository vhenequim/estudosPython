#Calculator

#Add
def add (n1, n2):
  return n1+n2

#Subtract
def subtract (n1, n2):
  return n1-n2

#Divide
def divide (n1, n2):
  return n1/n2

#Multiply
def multiply (n1, n2):
  return n1*n2

operations = {
  '+' : add,
  '-' : subtract,
  '/' : divide,
  '*' : multiply,
}

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
for symbols in operations:
  print (symbols)
symbol_selected = input("Choose an operation: " )
calc_operation = operations[symbol_selected]
awnser = calc_operation( num1, num2)
print (f"{num1} {symbol_selected} {num2} = {awnser}")
