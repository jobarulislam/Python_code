import wikipedia

print (f"Search for your topic..")

while True:
  topic =  input ("What is your topic? : ")
  result = wikipedia.summary( topic , sentences = 4)
  print (f"This is your search result :\n {result}") 
  s = input ("Do You search again? y/n : ")
  if s != "y":
    print (f"Thans for use .....")
    break
