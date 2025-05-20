class City:
  def __init__(self, name , nickname, found , country , population, landmarks):
    self.name = name
    self.nickname = nickname 
    self.found = found
    self.country = country
    self.population = population
    self.landmarks = landmarks

bagerhat = City("Bagerhat" , "Khalifatabad" , 1947 , "Bangladesh", 300000 , ["Shat Gombuj musque", "Khanjhan Ali Majar" , "Shunderbon"] )
alta = City("ALta" , "The City of the Northern Lights", 1863 , "Norway" , 21000 , ["Northern Lights Cathedral", "Alta Museum (World Heritage Rock Art Centre)", "the opportunity to witness the aurora borealis"])

print(vars(bagerhat))
print(vars(alta))
