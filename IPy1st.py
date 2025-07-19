print (f"Welcome Back \n Lets create a list of Expressions \n")
expression = []
while True:
  exp = input ("Add a expression : ")
  expression.append(exp)
  print (f"This is your List : {expression} ")
  ask = input ("DO you add more (y/n) : ")
  if ask != "y" :
    print (f"Have a good day!")
    break

