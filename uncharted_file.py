try: 
 sent_message = "Hey there! This is a secret message."

 with open("sent_message.txt","w" ) as file:
    file.write(sent_message)

 with open("sent_message.txt", 'r+') as file:
    original_message = file.read()
    content = file.read()
    print(content)
 unsent_message = "This message has been unsent."
 with open("sent_message.txt", "r+") as file:
    file.seek(0)
    
    file.write(unsent_message)
    file.truncate()
finally:
    file.close()

with open("sent_message.txt", "r") as file:
    content = file.read()
    print (content)
