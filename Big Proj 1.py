#achhabra 1188511

cart={}
#The book has a title, author, genre, and price
class Book:

    def __init__(self,title="",author="",genre="",price=0.0):
        self.title = title
        self.author= author
        self.genre=genre
        self.price=price
    def  __str__ (self):
        return "Title:"+self.title+"\n Author:"+self.author+"\n Genre:"+self.genre+"\n Price:"+self.price+"\n"

# The  inventory  has a collection of books for sale
class Inventory:
    def __init__(self):
        self.books={}
    def add_book(self):
        my_file = open('booklist.txt')
        data = my_file.readlines()
        data_count = len(data)
        for count in range(0, data_count):
            column = data[count].split(",")
            self.books [column[0]] = Book(column[1],column[2],column[3],column[4])

    def display (self):
        for number, book in self.books.items():
            print(''' Item Number:%s
 %s
 ====================================''' %(number, book))
            print("")    

class Cart (Inventory):
    def add_book(self,itemNumber,book=Book()):
        self.books [itemNumber] = book
    
    def checkout (self):
        totalPrice = 0.0;
        if len(self.books)== 0:
            print ("Your cart is empty.")
        else:         
            for number, book in self.books.items():
                totalPrice += float(book.price)
            print ("Your totsl purchase price is %s" %totalPrice)
        
    def displayCart (self):
        if len(self.books)== 0:
            print ("Your cart is empty.")
        else: 
            self.display()


#This is the while loop that runs until you quit
var=True
inventory = Inventory()
inventory.add_book()
cart = Cart()
while(var):
    
    store_menu=int(input('''What would you like

    1:display books
    2:add to cart
    3:show cart
    4:checkout
    5:quit
    '''))
    if store_menu==1 :
        inventory.display()
    elif store_menu==2:
        cartbook=input('Item Number:')
        cart.add_book(cartbook,inventory.books[cartbook])
    elif store_menu==3:
        cart.displayCart()
    elif store_menu==4:
        cart.checkout()

    elif store_menu==5:
        break
    else:
        print('please put in a choice')
                         
