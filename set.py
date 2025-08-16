#makeing set 
print ("<<<<<<<<<<<<<<<<<favorite fruits list of mine and my friend>>>>>>>>>>>>>>>")

my_fav_f = {'Grapes 🍇', 'Banana 🍌', 'Mango 🥭', 'Blueberries 🫐'}
friend_fav_f = {'Apple 🍎' , 'Pear 🍐' , 'Peach 🍑' , 'Cherries 🍒' , 'Strawberry 🍓' 'Blueberries 🫐'}

#union
union = my_fav_f.union(friend_fav_f)

#intersction
intersection = my_fav_f.intersection(friend_fav_f)

#difference
difference = my_fav_f.difference(friend_fav_f)

print (f"ALL the fruits : {union} " )
print (f"Common favorite fruits : {intersection} ")
print (f"My favorite fruits with out my friend favorites : {difference}")
print()
print ("==================================================================================================")
print ()
my_fav_f.add('Apple 🍎')
print (my_fav_f)
print ()
friend_fav_f.remove('Peach 🍑')
print (friend_fav_f)
