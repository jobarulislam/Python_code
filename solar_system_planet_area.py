from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
while True:
 random_planet = ch(planets)
 if random_planet == "Mercury":
   r = 2440
 elif random_planet == "Venus":
   r = 6052
 elif random_planet == "Earth":
   r = 6371
 elif random_planet == "Mars":
   r = 3390
 elif random_planet == "Saturn":
   r = 58232
 else:
   print (f"Oops! An error occurred..")          

 area = 4 * pi * r ** 2
 area = round(area)
 print (f"{random_planet} area is :  {area}")
 print ()
 a = input("Do you want to know an other planet area ? (y or n) : ")
 if a != "y":
   print("Thank You! See you again!....")
   break
