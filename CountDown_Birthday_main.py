import bday_message
from datetime import datetime , date


while True:
  print (f"Welcome to check your Birthday!")
  input ("Press Enter for start!")
  while True:
    birthday_input = input ("Enter your Birthday (YYYY,MM,DD): ")

    try:
      birthday = datetime.strptime(birthday_input , "%Y-%m-%d").date()
      break
    except ValueError :
      print (f"❌ Invalid date format. Please use YYYY-MM-DD and try again.\n")

  today = date.today()

  next_birthday = birthday.replace(year = today.year)
  if next_birthday < today:
      next_birthday = next_birthday.replace(year = today.year + 1 )

  days_left = (next_birthday - today).days 
  
  if next_birthday == today :
      print (bday_message.random_message())

  elif next_birthday > today:
      print (f"Your Next Birthday Is ON: {next_birthday} ")
      print (f"Days Remaing up coming Next Birthday : {days_left} days! ")

  else:
      print (f"ERROR......!")

  check_again = input ("Do you want to check again ('y' or 'n') : ")
  if check_again != "y":
      print (f"<<<<Thanks for use>>>>!")
      break 
