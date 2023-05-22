#Write a function called mult_list() to multiply all numbers in list

def mult_list():

  if len(li) == 0:
    return 0

  prod = li[0]

  if len(li) > 1:
    for i in li[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))