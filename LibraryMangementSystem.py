class library:
    def __init__(self,list,name):
        self.libbook = list
        self.libname = name
        self.libdict = {}

    def displayBooks(self):
        print(f"We have following bboks in our {self.libname} library : ")
        for books in self.libbook:
            print(books)


    def lendBooks(self,book,user):
        if book not in self.libdict.keys():
            self.libdict.update({book:user})
            print("User Data Updated")

        else:
            print(f"Sorry, Book is already taken by {self.libdict[book]}\n")

    def addBooks(self,book):
        self.libbook.append(book)
        print("Book Added")

    def returnBooks(self,book):
        self.libdict.pop(book)
        print("Book Return")


libworks = library(["Python", "Javascript", "Java", "C++", "Web Development"], "Codex")

while True:

    print(f"Welcome to {libworks.libname} Library. Enter Your Choice to Continue")
    print("1. Display Book")
    print("2. Lend Book")
    print("3. Add Books")
    print("4. Return Books")

    user_choice = input("Enter your choice : ")
    if user_choice not in ['1', '2', '3', '4']:
        print("Please Enter Valid Option")
        continue

    else:
        user_choice = int(user_choice)

    if user_choice==1:
        libworks.displayBooks()

    elif user_choice==2:
        book = input("Enter a book name you want : ")
        user = input("Enter your name : ")
        libworks.lendBooks(book,user)
        bookown = open("libbook.txt","w")
        bookown.write(user + " : " + book)

    elif user_choice==3:
        book = input("Add Book : ")
        libworks.addBooks(book)

    elif user_choice==4:
        book = input("Return Book : ")
        libworks.returnBooks(book)

    else:
        print("Invalid Input")
        

    print('''q. Quit
    c. Continue''')
    user_choice2 = input()

    if user_choice2=='q':
        exit()

    elif user_choice2=='c':
        continue
