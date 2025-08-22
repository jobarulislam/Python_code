#last part of data structures

players = [
  {'name' : 'Sakib', 'position' : 'CL' , 'j_number' : 15 , 'age' : 23, 'hight' : '5f6'},
  {'name' : 'Rubai', 'position' : 'SR', 'j_number' : 12, 'age' : 24, 'hight' : '5f11'},
  {'name' : 'Jobarul', 'position' : 'CR', 'j_number' : 27, 'age' : 25, 'hight' : '6f'},
  {'name' : 'Sabab', 'position' : 'SL', 'j_number' : 11, 'age' : 22, 'hight' : '5f6'},
  {'name' : 'Akib', 'position' : 'BG','j_number' : 7, 'age' : 25, 'hight' : '5f10'}
]
positions = [player["position"] for player in players]
print (f"Player Positions : {positions}")

for player in players :
   if player["name"] == "Sabab":
     player["age"] = 24
     player["position"] = "MF"
     print (f"Update of player : {player}")
     break

#calculation of player age 
cal = sum (player["age"] for player in players)
print (f"Total Age of players : {cal}")
