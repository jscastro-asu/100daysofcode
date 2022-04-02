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

num1 = int(input("Enter a number: "))

for ops in operations:
  print(ops)

#continue until user says "n"

end_operation = False
while not end_operation:
  
  ops_symbol = input("Choose an operation: ")
  num2 = int(input("Next number: "))
  calc = operations[ops_symbol]
  ans = calc(num1, num2)

  print(f" {num1} {ops_symbol} {num2} = {ans}")

  response = input(f"Continue calculating with {ans}? Type 'y' or 'n': ")

  if response == "n":
    print("Ok Bye")
    end_operation = True
  elif response == "y":
    num1 = ans






