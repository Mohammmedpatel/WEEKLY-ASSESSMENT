from helper import Md

def main():
    db=Md()
    while True:
        print("********WELCOME***********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit")
        print()
        try:
            choice=int(input())
            if(choice==1):
                uid=int(input("userid: "))
                usna=input("name : ")
                usph=input("phone : ")
                db.insert_user(uid,usna,usph)
            elif choice==2:
                db.fetch_all()
            elif choice==3:
                uid=int(input("userid to delete: "))
                db.delete_user(uid)
            elif choice==4:
                uid=input("userid of user you want to update : ")
                usna=input("new name : ")
                usph=input("new phone : ")
                db.update_user(uid,usna,usph)
            elif choice==5:
                break
            else:
                print("Invalid input ! Try again.")
        except Exception as e:
            print(e)
            print("Invalid detail ! Try again.")       

if __name__=="__main__":
    main()
             