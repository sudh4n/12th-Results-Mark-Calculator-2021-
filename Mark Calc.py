# 10th Mark Calculation

print("12th Mark Calculator by SUDHAN ")

Marks1 = int(input("Enter Your Marks 1 "))
Marks2 = int(input("Enter Your Marks 2 "))
Marks3 = int(input("Enter Your Marks 3 "))

tot = Marks1 + Marks2 + Marks3

avg = tot / 3 / 2

print("Your 10th Marks(50%) is", avg)

# 11th Mark Calculation

Tamil = int(input("Enter Your Tamil Marks "))
English = int(input("Enter Your  English Marks "))
Maths = int(input("Enter Your Maths Marks "))
Physics = int(input("Enter Your Physics Marks "))
Chemistry = int(input("Enter Your Chemistry Marks "))
CS = int(input("Enter Your CS Marks "))

Tamil2 = Tamil / 90
print("Your 11th Tamil Mark is", Tamil2.__mul__(20))

English2 = English / 90
print("Your 11th English Mark is", English2.__mul__(20))

Maths2 = Maths / 90
print("Your 11th Maths Mark is", Maths2.__mul__(20))

Physics2 = Physics / 70
print("Your 11th Physics Mark is", Physics2.__mul__(20))

Chemistry2 = Chemistry / 70
print("Your 11th Chemistry Mark is", Chemistry2.__mul__(20))

CS2 = CS / 70
print("Your 11th CS Mark is", CS2.__mul__(20))

# 12th Mark Calculation

Tamil = int(input("Enter Your Tamil Marks "))
English = int(input("Enter Your  English Marks "))
Maths = int(input("Enter Your Maths Marks "))
Physics = int(input("Enter Your Physics Marks "))
Chemistry = int(input("Enter Your Chemistry Marks "))
CS = int(input("Enter Your CS Marks "))

Tamil1 = Tamil / 10
print("Your Tamil Mark is", Tamil1.__mul__(30))

English1 = English / 10
print("Your Englsh Mark is", English1.__mul__(30))

Maths1 = Maths / 10
print("Your Maths Mark is", Maths1.__mul__(30))

Physics1 = Physics / 30
print("Your Physics Mark is ", Physics1.__mul__(30))

Chemistry1 = Chemistry / 30
print("Your Chemistry Mark is", Chemistry1.__mul__(30))

CS1 = CS / 30

print("Your CS Mark is ", CS1.__mul__(30))

# Total Subject Mark

print("Your 12th Tamil Mark is ", avg + Tamil2.__mul__(20) + Tamil1.__mul__(30))

print("Your 12th English Mark is ", avg + English2.__mul__(20) + English1.__mul__(30))

print("Your 12th Maths Mark is ", avg + Maths2.__mul__(20) + Maths1.__mul__(30))

