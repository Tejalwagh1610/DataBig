# How to use if-else in Python

x = 10
y = 5

if x==y:
    print("Yes x is equals to y!!")
else:
    print("No, x is not Equals to y!!")

# is it mandetory to use the else block with if block?

# a = 50
# if a==50:
#     print("Yes, a is equals to 50!!")
# print("Bye!!")

a = 40
if a==50:
    print("Yes, a is equals to 50!!")
print("Bye!!")

# Nested IF-Else
marks = 58

if marks>=90:
    print("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A")
elif marks>=70 and marks<88:
    print("Grade B")
else:
    print("Grade C")
