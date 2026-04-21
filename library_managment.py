"""Library Managment system"""
import uuid
import os
import json
import csv
from datetime import datetime , timedelta


FILE_NAME = "book_data.json"
MEMBER_DATA = "member_data.json"
ISSUE_DATA = "issue_data.json"


def load_all_member():
    if not os.path.exists(MEMBER_DATA):
        return {}
    with open(MEMBER_DATA, "r") as f:
        return json.load(f)

def load_all_issue():
    if not os.path.exists(ISSUE_DATA):
        return {}
    with open(ISSUE_DATA, "r") as f:
        return json.load(f)


def load_all_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_all_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def save_all_member(data):
    with open(MEMBER_DATA, "w") as f:
        json.dump(data, f, indent=4)

def save_all_issue(data):
    with open(ISSUE_DATA, "w") as f:
        json.dump(data, f, indent=4)


class Books():
    def __init__(self, title, author, genre, total_cp, available_cp, isbn_no, publish_year, shelf):
        data = load_all_data()

        for b in data.values():
            if b["title"].lower() == title.lower():
                print("Book already exists")
                return

    
        self.book_id = str(uuid.uuid4())[:8]    
        self.title = title
        self.author = author
        self.genre = genre
        self.total_cp = total_cp
        self.available_cp = available_cp
        self.isbn_no = isbn_no
        self.publish_year = publish_year
        self.shelf = shelf
        self.save()
        print(f"New Book with id : {self.book_id}")

    def save(self):
        data = load_all_data()

        data[self.book_id] = {
            "book_id":self.book_id,
            "title":self.title,
            "author": self.author,
            "genre": self.genre,
            "total copies": self.total_cp,
            "available copies":self.available_cp,
            "isbn no":self.isbn_no,
            "publish year":self.publish_year,
            "shelf":self.shelf
        }

        save_all_data(data)


    @classmethod
    def update_book(cls):
        data = load_all_data()

        book_id = input("Enter Book ID: ")

        if book_id not in data:
            print(" Invalid ID")
            return

        book = data[book_id]

        print("Leave blank to keep old value")

        new_title = input("New title: ")
        new_author = input("New author: ")
        new_genre = input("New genre: ")
        new_total = input("New total copies: ")

        if new_title:
            book["title"] = new_title
        if new_author:
            book["author"] = new_author
        if new_genre:
            book["genre"] = new_genre
        if new_total:
            diff = int(new_total) - int(book["total copies"])
            book["total copies"] = int(new_total)
            book["available copies"] = (diff + int(book["available copies"]))

        save_all_data(data)
        print(" Updated successfully")


    @classmethod
    def remove_book(cls):
        data = load_all_data()

        if not data:
            print(" No books available")
            return

        # show books
        # for bid, b in data.items():
        #     print(f"{bid} -> {b['title']}")

        book_id = input("Enter Book ID to remove: ")

        if book_id not in data:
            print(" Invalid Book ID")
            return

        # if int(data[book_id]["available copies"]) < int(data[book_id]["total copies"]):
        #     print("Cannot delete issued book")
        #     return

        data.pop(book_id)
        save_all_data(data)

        print(" Book removed")


    @classmethod
    def view_all_book(cls):
        data = load_all_data()

        if not data:
            print("No books available")

        for bid , b in data.items():
            print(f"""
            Book id : {bid}
            Book title : {b['title']}
            Book author : {b['author']} 
            Available Copies : {b['available copies']}
            """)

    @classmethod
    def view_available_books(cls):
        data = load_all_data()

        found = False
        for bid, b in data.items():
            if int(b["available copies"]) > 0:
                print(f"{bid} | {b['title']} ({b['available copies']} available)")
                found = True

        if not found:
            print(" No available books")

    @classmethod
    def view_books_genre(cls,genre):
        data = load_all_data()

        found = False
        for bid, b in data.items():
            if b['genre'].lower() == genre.lower():
                print(f"{bid} | {b['title']}")
                found = True

        if not found:
            print(" No available books")

    # @classmethod
    # def import_csv(cls):
    #     filename = input("Enter CSV file: ")

    #     if not os.path.exists(filename):
    #         print(" File not found")
    #         return

    #     data = load_all_data()

    #     with open(filename, newline="") as f:
    #         reader = csv.DictReader(f)

    #         for row in reader:
    #             duplicate = False
    #             for b in data.values():
    #                 if b["isbn no"] == row["isbn"]:
    #                     duplicate = True
    #                     break

    #             if not duplicate:
    #                 book = Books(
    #                     row["title"],
    #                     row["author"],
    #                     row["genre"],
    #                     row["total"],
    #                     row["isbn"],
    #                     row["year"],
    #                     row["location"]
    #                 )

    #     print("CSV import done")




#!Member cls

class Member():
    def __init__(self,name, phone, email, member_type):
        data = load_all_member()

        for b in data.values():
            if b["name"].lower() == name.lower():
                print("Member already exists")
                return

    
        self.member_id = str(uuid.uuid4())[:8]    
        self.name = name
        self.phone = phone
        self.email = email
        self.member_type = member_type
        self.join_date = datetime.now()
        self.status = "Active"
        self.exp_date = datetime.now() + timedelta(days=1)
        self.save()
        print(f"New Member with id : {self.member_id}")
    
    def save(self):
        data = load_all_member()

        data[self.member_id] = {
            "member_id":self.member_id,
            "name":self.name,
            "phone": self.phone,
            "email": self.email,
            "member type": self.member_type,
            "joining date":self.join_date.day,
            "exp date":self.exp_date.day,
            "status" : self.status,
            "issued no of books":0,
            "issued book name":[],
            "fine" : 0
        }

        save_all_member(data)

    @classmethod
    def remove_member(cls):
        data = load_all_member()

        if not data:
            print(" No member available")
            return

        member_id = input("Enter Member ID to remove: ")

        if member_id not in data:
            print(" Invalid Member ID")
            return

        data.pop(member_id)
        save_all_member(data)

        print(" Member removed")

    @classmethod
    def view_all_member(cls):
        data = load_all_member()

        if not data:
            print("No Member available")

        for mid , m in data.items():
            print(f"""
            member id : {mid}
            Member name : {m['name']}
            Member phone : {m['phone']} 
            Member type : {m['member type']}
            """)

    @classmethod
    def update_member(cls):
        data = load_all_member()

        member_id = input("Enter Member ID: ")

        if member_id not in data:
            print(" Invalid ID")
            return

        member = data[member_id]

        print("Leave blank to keep old value")

        # new_title = input("New title: ")
        new_phone = input("New phone: ")
        new_email = input("New email: ")
        # new_total = input("New total copies: ")

        # if new_title:
        #     book["title"] = new_title
        if new_phone:
            member["phone"] = new_phone
        if new_email:
            member["email"] = new_email
        

        save_all_member(data)
        print(" Updated successfully")


class Issue_Return():
    def __init__(self,book_id,member_id):
        self.issue_id = str(uuid.uuid4())[:8]    
        self.issue_date = datetime.now()
        self.due_date = datetime.now() + timedelta(days=7)
        self.renewal = 0
        self.book_id = book_id
        self.member_id = member_id
        self.save()


    @classmethod
    def issue_book(self):
        book_data = load_all_data()
        member_data = load_all_member()
        book_id = input("Enter book ID to issue : ")

        if book_id not in book_data:
            print(" Invalid ID")
            return

        member_id = input("Enter member ID to issue : ")
        if member_id not in member_data:
            print("Invalid ID")
            return
        
        book = book_data[book_id]
        member = member_data[member_id]

        if (member["issued no of books"] >= 2 and member["member type"] == "Student") or (member["issued no of books"] >= 5 and member["member type"] == "Teacher") or (member["issued no of books"] >= 1 and member["member type"] == "External"):
            print("You already issued all the books you can !! return 1 book to issue new book !")

        elif member["status"] == "Deactivate":
            print("Your Status is deactivated. You can't issue book")

        elif member["fine"] > 0 :
            print(f"You have unpaid fine of {member["fine"]} , pay the amount first to issue the book")
        
        elif book["available copies"] <=0 :
            print(f"No copies available for the book {book["title"]}")

        for b in member["issued book name"]:
            if book["title"] == b:
                print("you already have that book")
                return

        # print(book)
        member["issued no of books"] += 1
        member["issued book name"].append(book["title"])
        book["available copies"] -= 1
        
        save_all_data(book_data)
        save_all_member(member_data)


        obj = Issue_Return(book['book_id'] , member['member_id'])


        
    def save(self):
        data = load_all_issue()

        data[self.issue_id] = {
            "book":self.book_id,
            "member": self.member_id,
            "issue date": self.issue_date.day,
            "due date": self.due_date.day,
            "renewal":self.renewal
        }

        save_all_issue(data)


        


class Fine():
    pass

class Report():
    pass

class Admin():
    pass



#--------------Main Menu---------------------

while True:
    print('-'*25)
    print("1. Book Management")
    print("2. Member Management")
    print("3. Issue & Return")
    print("4. Fine & Payments")
    print("5. Reports & Search")
    print("6. Admin Settings")
    print("0. Exit")
    print('-'*25)

    choice = int(input("Enter your Choice : "))

    #! book managment system
    if choice == 1:
        while True:        
            print('-'*25)
            print("1. Add new book",
                    "2. Remove book",
                    "3. Update book details",
                    "4. View all books",
                    "5. View available books only",
                    "6. View books by category/genre",
                    "7. Add multiple books from CSV import",
                    "8. Back",sep="\n")
            print('-'*25)

            book_ch = int(input("Enter your Choice : "))

            if book_ch == 1:
                print('-'*25)
                print("Enter following book details : ")
                title = input("Enter title : ")
                author = input("Enter author : ")
                genre = input("Enter genre : ")
                total_copies = int(input("Enter total copies : "))
                available_copies = int(input("Enter available copies : "))
                isbn_no = int(input("Enter isbn no : "))
                publication_year = int(input("Enter publication year : "))
                shelf = input("Enter shelf location : ")
                print('-'*25)

                book1 = Books(title, author, genre, total_copies, available_copies, isbn_no, publication_year, shelf)

            elif book_ch ==2:
                Books.remove_book()
                
            elif book_ch == 3:
                Books.update_book()


            elif book_ch == 4:
                
                Books.view_all_book()

            elif book_ch == 5:
                Books.view_available_books()

            elif book_ch == 6:
                genre = input("Enter the genre : ")
                Books.view_books_genre(genre)

            elif book_ch == 7:
                # Books.import_csv()
                pass
            
            elif book_ch == 8:
                break

            else:
                print("Select valid option")
            
    #! Member managment system

    elif choice == 2:
        while True:
            print('-'*25)
            print("1. Register new member",
                  "2. Remove member",
                  "3. Update member details",
                  "4. View all members",
                  "5. View member profile (books issued, fines, history)",
                  "6. Activate / Deactivate member",
                  "7. Back",
                    sep="\n"
                    )
            print('-'*25)

            member_ch = int(input("Enter your choice : "))
            
            if member_ch == 1:
                print('-'*25)
                print("Enter following  details : ")
                name = input("Enter Name : ")
                phone = input("Enter phone : ")
                email = input("Enter email : ")
                member_type = input("Enter member type(Student/ Teacher / External) : ")
                print('-'*25)

                member1 = Member(name,phone,email,member_type)

            elif member_ch == 2:
                Member.remove_member()

            elif member_ch == 3:
                Member.update_member()

            elif member_ch == 4:
                Member.view_all_member()

            elif member_ch == 5:
                pass
            elif member_ch == 6:
                pass
            elif member_ch == 7:
                break

            else:
                print("Enter valid choice : ")



    #!Issue menu

    elif choice == 3:
        while True:
            print('-'*25)
            print("1. Issue book to member",
                  "2. Return book",
                  "3. Renew book (extend due date)",
                  "4. View all currently issued books",
                  "5. View overdue books",
                  "6. Back",
                    sep="\n"
                    )
            print('-'*25)

            issue_ch = int(input("Enter your choice : "))
            
            if issue_ch == 1:
                Issue_Return.issue_book()
            else:
                break

    #! Fine menu
    elif choice == 4:
        while True:
            print('-'*25)
            print("1.  Check fine for a member",
                  "2. Pay fine",
                  "3. View all pending fines",
                  "4. Fine history of a member",
                  "5. Back",
                    sep="\n"
                    )
            print('-'*25)

            fine_ch = int(input("Enter your choice : "))
            
            if fine_ch == 1:
                pass
            else:
                break

    #!Reports & Search menu
    elif choice == 5:
        while True:
            print('-'*25)
            print("1. Search book by title / author / ISBN / genre",
                  "2. Search member by name / ID / phone",
                  "3. Most issued books (Top 5)",
                  "4. Members with highest fines",
                  "5. Books never issued (dead stock)",
                  "6. Monthly issue report (by month input)",
                  "7. Overdue report (all overdue + fine amount)",
                  "8. Back",
                    sep="\n"
                    )
            print('-'*25)

            report_ch = int(input("Enter your choice : "))
            
            if report_ch == 1:
                pass
            else:
                break

    #! Admin menu
    elif choice == 6:
        while True:
            print('-'*25)
            print("1. Change fine rate (₹ per day)",
                  "2. Change max issue days",
                  "3. Change max books per membership type",
                  "4. View system stats (total books, members, issued, fines collected)",
                  "5. Backup data (copy JSON to backup folder with timestamp)",
                  "6. Back",
                    sep="\n"
                    )
            print('-'*25)

            admin_ch = int(input("Enter your choice : "))
            
            if admin_ch == 1:
                pass
            else:
                break


    else:
        break




    