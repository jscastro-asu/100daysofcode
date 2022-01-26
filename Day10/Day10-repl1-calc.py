def add(n1, n2):
      return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

for ops in operations:
  print(ops)
ops_symbol = input("Choose an operation above: ")

# new function: tap into the dict and take the symbol
calc = operations[ops_symbol]
answer = calc(num1, num2)

print(f" {num1} {ops_symbol} {num2} = {answer}")
