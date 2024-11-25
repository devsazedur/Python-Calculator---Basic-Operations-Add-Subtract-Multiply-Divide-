# function for each operation
def add(a,b):
  return a + b

def  subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

# main calculator function
def calculator():

  # starting messages
  print("Welcome to python Calculator!")
  print("Available operations: add, subtract, multiply, divide")

  # get user input
  num1 = float(input("Enter first number:"))
  num2 = float(input("Enter secund number: "))
  operation = input("Select Operation: add, subtract, multiply, divide: ")

  if operation == "add":
    result = add(num1, num2)

  elif operation == "subtract":
    result = subtract(num1, num2)

  elif operation == "multiply":
    result = multiply(num1, num2)

  elif operation == "divide":
    result = divide(num1, num2)

  else:
    print("Invalid operation!")

  # Remove decimals for whole numbers.
  if isinstance(result, float) and result.is_integer():
    result= int(result)

  print(f"The result is: {result}")

# call the main calculator function
calculator()
