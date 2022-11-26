# Numerical operators in Python

# + for Addition
# - for Subtraction
# * for multiplication
# / for Division
# // for Integer division
# ** for power calculations
# % for Modulus

x = 5
y = 3
print("Addition of x,y = ", x+y)
print("Subtraction of x,y = ", x-y)
print("Multiplition of x,y = ", x*y)
print("Divion of x,y = ", x/y)
print("Integer Division of x,y = ", x//y)
print("Modulus of x,y = ", x%y)
print("x to the power y = ", x**y)

# Some operations of strings
str_data = "Tejal"
empty_str = ' '

#Concat operation for strings
# The '+' symbol acts as a concatanation operatorin python
# If we use '-' symbol then error (unsupported) will appear As it is not defined
full_name = str_data + " " + "Wagh"
print("Full Name: ", full_name)

multiply_numeric_str = "Tejal Wagh, " * 5
print("Print multiply numeric str: ", multiply_numeric_str)


# Assignment Operators 
# =, x = 5
# +=, x += 5 -> x = x + 5
# -=, x -= 5 -> x = x - 5
# *=, x *= 5 -> x = x * 5
# /=, x /= 5 -> x = x / 5
# //=, x //= 5 -> x = x // 5
# %=, x %= 5 -> x = x % 5

# Comparision Operators 
# == , Equals to condition, x==y
# != , Not Equals to condition, x!=y
# > , Greater than condition, x<y
# < , Less than condition, x>y
# >= , Greater than Equals to condition, x>=y
# <= , Less than Equals to condition, x<=y

a = 18
b = 5
print(" Result for a==b is : ", a==b)
print(" Result for a!=b is : ", a!=b)
print(" Result for a>b is  : ", a>b)
print(" Result for a<b is  : ", a<b)
print(" Result for a>=b is : ", a>=b)
print(" Result for a<=b is : ", a<=b)


# Logical Operators (Here we try to compare the final result of expression)
# and -> Returns True if both the Statements are True
# or -> Returns True if one of the Statements is True
# not -> Reverse the Result, returns False if the result is True

m = 10
n = 8
print("If m>10 and n<10 Result", m>10 and n<10) # False and True -> False
print("If m>20 or n<10 Result", m>10 or n<10) # False or True -> True
print("If m>10 not n<10 Result", not(m>10 and n<10))
# not(False and True) -> not(False) ->True
