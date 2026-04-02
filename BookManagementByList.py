lis = []
def menu():
    print("*** MAIN MENU ***")
    print("0. Exit")
    print("1. Add new book")
    print("2. List all books")
    print("3. Search by ID")
    print("4. Delete a book")

    return int(input("Enter your choice: "))


def addbook():
    bId = input("Enter Book Id : ")
    bName = input("Enter Book Name : ")
    bAuthor = input("Enter Book Author : ")
    bPrice = float(input("Enter Book Price : "))
    new_Book = (bId, bName, bAuthor, bPrice)
    lis.append(new_Book)
    print("Book Added..!!!")

def DisplayBook():
    if len(lis)==0:
        print("No Database, Please add Records..!!")
    else:
        for i in lis:
            print(i)

def RemoveBook():
    inp = input("Enter Book Id")
    found = False
    for i in range(len(lis)):
        if lis[i][0]==inp:
            lis.pop(i)
            print("Book Removed..!!")
        else:
            print("Book Not Found")

def SearchBook():
        search = input("Enter Book you want to search : ") 
        for i in lis:
            if search == i:
                print("Book is - ")
                print(i)

def main():  
    while True:
        choice = menu()

        if choice == 0:
            break
        if choice <0 or choice > 4:
            print("Invalid choice. Please try again.")
            continue
        if choice == 1:
            addbook()
        elif choice == 2:
            DisplayBook()
        elif choice == 3:
            SearchBook()
        else:
            RemoveBook()

        print("Hit ENTER/RETURN key to continue")
        input()

main()
