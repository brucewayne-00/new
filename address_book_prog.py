
address_book={}

def create():
    name=input("enter name : ")
    phone=input("enter phone no. : ")
    address_book[name]=phone
    print(" contact created successfully !")

def view():
    if not  address_book:
        print(" No contacts to display !")
    else:
        for name, phone in address_book.items():
            print(f" {name} : {phone}")


def delete():
     name=input(" enter name to delete : ")
     if name in address_book:
         del address_book[name]
     print(" contact deleted successfully !")

def modify():
    name=input(" enter name to modify contact : ")
    if name in  address_book:
        phone=input("enter phone no. : ")
        address_book[name]=phone
    print("contact modified successfully !")

while True:
    print("\n a)create b)view c)delete d)modify e)exit")
    choice=input("enter choice : ")
    if choice=='a':
        create()
    elif choice=='b':
        view()
    elif choice=='c':
        delete()        
    elif choice=='d':
        modify()
    elif choice=='e':
        print("thank you !")
        break          
        