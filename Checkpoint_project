# createing checkpoint project 
import random

fate = ["life", "death"]
fate1 = ["home","death"]

name = input("Hello Explore! Let's start with your Name : ")
print ()
print ("Welcome Explor " + name +" The Gelaxy Of Wonder\n ")
print ("Choose Carefully! If you choose wrong Planet It Can Take your Life "+ name)
print ()
hp = 100

print ( name + " this is your Helth point : " , hp)

print ()

print ("If your HP is become 0 then you will die!")

r = int(input(" Are You Ready?\n 1.yes 2.no "))

if r == 1:
  print ("Lets Start! Choose a Planet : \n")
  print ("1. This is planet of Harkulis.")
  print ("2. This is planet of Eger.") 
  c = int (input("Choose a Planet! 1 or 2 : "))
  if c == 1:
      print (" You get Two Mistrey Box! \n 1.Red Box\n 2.Blue Box\n 3.skip ")
      c1 = int (input("CHoose A Box : "))
      if c1 == 1:
         print ("you get 20 more HP\n")
         hp += 20
         print (f"Now your Hp is : {hp}\n ")
         ch = int (input ("Choose a option : \n 1.Go to 3rd Planet\n 2.Go to 4th Planet "))
         if ch == 1:
            print ("Wellcome to Orion! Becarefull This is the planet of iliution. Don't Trast anything Without bing sure about it.\nAll The Best.")
            dm1 = random.choice(fate)
            if dm1 == "life":
               print ("Congratuletion! you find the path of erth .")
            else: 
               print ("You diead")
               print ("Game Over.") 
         else:
            print ("Wellcome to Halli The planet of mystreouse creature.They can attack you or hell you")
            dm3 = random.choice(fate)
            if dm3 == "life":
               print (f"Go Home!")
            else:
               print (f"Game Over!")
      elif c1 == 2:
         dm = random.randint(20, 50)
         print ("This Box is full of Poisonass gas !")
         hp -= dm
         print (f"Your HP is now : {hp} ")
      else:
         print (f"You skip the mystrey box! Lets explore another planet!")
         ch = int (input ("Choose a option : \n 1.Go to 5th Planet\n 2.Go to 6th Planet "))
         if ch == 1:
            print ("Wellcome to Athen! Becarefull This is the planet of iliution. Don't Trast anything Without bing sure about it.\nAll The Best.")
            dm1 = random.choice(fate)
            if dm1 == "life":
               print ("Congratuletion! you find the path of erth .") 
            else: 
               print ("Game Over.") 
         else:
            print ("Wellcome to malli The planet of mystreouse creature.They can attack you or hell you")     
            c3 = int (input("Choose A Path:\n 1. hell \n 2. heven"))
            if c3 == 2:
               dm2 = random.randint(30,90)
               hp -= dm2
               print (f"new Hp IS : {hp}")
            else:
               ch1 = random.choice(fate1)
               if ch1 == "home":
                 print (f"You are going Home {name}")
               else:
                 print (f"Game Over")
  else:
    print (f"This Planet I poisonass.Yor life in denger.Evacuate Fast otherwise you will killed.")
    hp -= 50
    c2 = int(input("for evacute input 1 : "))
    if c2 == 1:
       print (f"You are Evacuted!\n")
       print (f"Now your Hp is : {hp}\n")
       c1 = int (input("CHoose A Box :\n 1. red\n 2. blue\n 3.Black "))
       if c1 == 1:
         print ("you get 20 more HP\n")
         hp += 20
         print (f"Now your Hp is : {hp}\n ")
         ch = int (input ("Choose a option : \n 1.Go to 3rd Planet\n 2.Go to 4th Planet "))
         if ch == 1:
            print ("Wellcome to Orion! Becarefull This is the planet of iliution. Don't Trast anything Without bing sure about it.\nAll The Best.")
            dm1 = random.choice(fate)
            if dm1 == "life":
               print ("Congratuletion! you find the path of erth .")
            else: 
               print ("You diead")
               print ("Game Over.") 
         else:
            print ("Wellcome to Halli The planet of mystreouse creature.They can attack you or hell you")
            dm3 = random.choice(fate)
            if dm3 == "life":
               print (f"Go Home!")
            else:
               print (f"Game Over!")
       elif c1 == 2:
         dm = random.randint(20, 50)
         print ("This Box is full of Poisonass gas !")
         hp -= dm
         print (f"Your HP is now : {hp} ")
       else:
         print (f"You skip the mystrey box! Lets explore another planet!")
         ch = int (input ("Choose a option : \n 1.Go to 5th Planet\n 2.Go to 6th Planet "))
         if ch == 1:
            print ("Wellcome to Athen! Becarefull This is the planet of iliution. Don't Trast anything Without bing sure about it.\nAll The Best.")
            dm1 = random.choice(fate)
            if dm1 == "life":
               print ("Congratuletion! you find the path of erth .") 
            else: 
               print ("Game Over.") 
         else:
            print ("Wellcome to malli The planet of mystreouse creature.They can attack you or hell you")     
            c3 = int (input("Choose A Path:\n 1. hell \n 2. heven"))
            if c3 == 2:
               dm2 = random.randint(30,90)
               hp -= dm2
               print (f"new Hp IS : {hp}")
            else:
               ch1 = random.choice(fate1)
               if ch1 == "home":
                 print (f"You are going Home {name}")
               else:
                 print (f"Game Over")
    else:
       print (f"Your hp Is Become 0 and you are killed!")
       print (f"Game Over!\n All The Best for next Time!")  
  if hp <= 0:
    print (f"Game Over")
  else:
    print (f"Your HP is now : {hp}\n Congratulation Your going home safely")
else:
  print (f"Comeback when you ready!")
