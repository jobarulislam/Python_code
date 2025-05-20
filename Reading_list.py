books = ["Harry Potter","1984","The Fault in Our Stars","The Mom Test","Life in Code"]
print (books)

print ("Lets Add the book")
add = input ("Book name : ")
books.append(add)
print (books)
#remove books 

print ("Lets remove a book from list")
rm = input ("Book name : ")
books.remove(rm)
print (books)

# pop the book
print (" Lets remove The books by its index.")
p = int (input ("Give The Index : "))
books.pop(p)
print (books)
