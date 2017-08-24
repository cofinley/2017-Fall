# Connor Finley
# Advanced Python
# Assignment 1 - Collatz Sequence
# Date: 2017/08/23


def collatz(number):
  if number % 2 == 0:
    result = number // 2
  else:
    result = 3*number + 1
  print(result)
  return result


def collatz_sequence():
  try:
    term = int(input("Enter the first term of the sequence:"))
    while term != 1:
      term = collatz(term)
    return True
  except ValueError:
    print("Invalid input: must be an int")
    return False

collatz_sequence()