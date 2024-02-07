import random
import string

def generate_password(length, complexity):
  """Generates a password based on length and complexity requirements."""
  
  # Define character sets based on complexity level
  chars = {
    'low': string.ascii_lowercase,
    'medium': string.ascii_lowercase + string.digits,
    'high': string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
  }

  # Get character set based on user input
  char_set = chars[complexity.lower()]

  # Generate password with random characters from the chosen set
  password = ''.join(random.choice(char_set) for _ in range(length))

  return password

while True:
  # Get user input for length and complexity
  length = int(input("Enter desired password length: "))
  complexity = input("Choose complexity (low, medium, high): ")

  # Generate and display password
  password = generate_password(length, complexity)
  print(f"Your generated password: {password}")

  # Ask if user wants to generate another password
  choice = input("Generate another password? (y/n): ")
  if choice.lower() != 'y':
    break

print("Password generator closed.")
