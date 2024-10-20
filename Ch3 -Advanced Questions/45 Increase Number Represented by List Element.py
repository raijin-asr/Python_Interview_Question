
# define a function to add 1 to the number
# represented by the digits list
def add_one(digits):
  
  # adding 1 to last digit and
  # getting carry
  # also replacing last digit with remainder
  digits[-1] += 1
  carry = digits[-1] // 10
  digits[-1] = digits[-1] % 10

  # continue adding carry to
  # each digit from second last element
  # to first element
  for d in range(len(digits) - 2, -1, -1):
    if carry:
      digits[d] += 1
      carry = digits[d] // 10
      digits[d] = digits[d]% 10

  # even after adding all carry
  # if one carry is still remaining
  # we need to add that digit
  # at beginning
  if carry:
    digits.insert(0,carry)
  
  # return the final list
  return digits


digits = [8, 9, 9]
added_digits = add_one(digits)
print(added_digits)