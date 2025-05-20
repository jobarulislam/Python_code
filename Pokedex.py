class Pokemon:
  def __init__(self, entry , name , types , hight, category, weight , abilities , gender , weaknesses , description , is_caught):
      self.entry = entry
      self.name = name
      self.types = types
      self.hight = hight
      self.category = category
      self.weight = weight
      self.abilities = abilities
      self.gender = gender
      self.weaknesses = weaknesses
      self.description = description
      self.is_caught = is_caught

  def speak(self):
     print (f"Pokemon sound : {self.name} {self.name} ")

  def display_details(self):
      print(f"Entry Number    : {self.entry}")
      print(f"Name Of Pokemon : {self.name} ")
      print(f"")
      print(f"") 
      print(f"   Hight           Category   ")
      print(f"{self.hight}   {self.category}")
      print(f"")
      print(f"   Weight         Abilities   ")
      print(f"{self.weight}lb {self.abilities}")
      print(f"")
      print(f"   Gender    ")
      print(f"{self.gender}")
      print(f"")
      print(f"Type")
      print(f"{self.types}")
      print(f"")
      print(f"Weaknesses")
      print(f"{self.weaknesses}")
      print(f"")
      print(f"Description")
      print(f"{self.description}. {self.name} has already been {self.is_caught}!")
      print(f"")


ekans = Pokemon(23 , "Ekans" , ["Poison","gas" ] , " 6f 07inc " , "Snake", 15.2 ,["Shed Skin", "Intimidate"], ["male", "Female"],["Graound ","Psychic"] , "It can freely detach its jaw to swallow large prey whole. It can become too heavy to move, however.", True)
       
pikachu = Pokemon(25 , "Pikachu" ,["Electric" , "Thander"], "1f 04inc", "Mouse", 13.2 , ["Static",], ["Male", "Female"], ["Graound", ] , "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks." , True)

eevee = Pokemon(133 , "Eevee" ,["Normal",], "1f 00inc", "Evolution", 14.3 , ["Run away","Adaptability"], ["Male", "Female"], ["Fighting" , ], "Its ability to evolve into many forms allows it to adapt smoothly and perfectly to any environment." , False)

ekans.display_details()
ekans.speak()
pikachu.display_details()
pikachu.speak()
eevee.display_details()
eevee.speak()
