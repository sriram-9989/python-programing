def calculate(num1, num2, operator):
  """Performs the calculation based on the operator."""
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Division by zero!"
    else:
      return num1 / num2
  else:
    return "Invalid operator!"

while True:
  # Get user input
  num1 = float(input("Enter first number: "))
  operator = input("Enter operator (+, -, *, /): ")
  num2 = float(input("Enter second number: "))

  # Perform calculation and display result
  result = calculate(num1, num2, operator)
  print(f"{num1} {operator} {num2} = {result}")

  # Ask if user wants to continue
  choice = input("Do another calculation? (y/n): ")
  if choice.lower() != 'y':
    break

print("Calculator closed.")
