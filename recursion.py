# Find the first uppercase letter in a given string
def find_upper_case(inputStr, i=0):
    if inputStr[i].isupper():
        return inputStr[i]
    if i == len(inputStr) - 1:
        return "No upper case found :/"
    return find_upper_case(inputStr, i+1)


#Calculate the length of a string
def len_str(string):
    if string == "":
        return 0
    return 1 + len_str(string[1:])


# Count the number of consonants in a string aka not (a,e,i,o,u)
def count_consonants(string):
    vowels = ["a", "e", "i", "o", "u"]
    if string == "":
        return 0 
    if string[0].lower() not in vowels and string[0].isalpha():
        return 1 + count_consonants(string[1:])
    return count_consonants(string[1:])
        
#Multiplication recursion mode
def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    return a + multiply(a, b - 1)

# Sum of  a list of numbers 
def sumList(lst):
  if lst == []:
    return 0
  return lst[0] + sumList(lst[1:])


# An integer to a base
def convertBase(integer, base):
  convert = '0123456789ABCDEF'
  if integer < base:
    return convert[integer]
  return convertBase(integer//base, base) + convert[integer%base]

#Sum the integers in a list that contains lists
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total

# Factorial of a non negative number 
def factorial(n):
  if n < 0:
    return None
  if n == 0 or n == 1:
    return 1
  return n * factorial(n - 1)

# Sequence of fibonnaci
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

# Sum of digits of an integer
def sumDigits(n):
  if n == 0:
    return 0 
  return n % 10 + sumDigits(n // 10)

# Power of a number
def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
