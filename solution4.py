# Write a function called num_within() to check whether a number falls in a given range

def num_within(x,a,b):
      return x in range(a,b+1)
     
print(num_within(3,4,5))     
print(num_within(6,7,8))     
print(num_within(9,10,11))