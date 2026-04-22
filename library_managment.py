"""Library Managment system"""
import uuid
import os
import json
import csv
import zipfile
from datetime import datetime , timedelta

FILE_NAME = "book_data.json"
MEMBER_DATA = "member_data.json"
ISSUE_DATA = "issue_data.json"
FINE_DATA = "fine_data.json"
BACKUP_DATA = "backup_data.json"
ADMIN_RULE = "admin_rule.json"


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

def load_all_fine():
    if not os.path.exists(FINE_DATA):
        return {}
    with open(FINE_DATA, "r") as f:
        return json.load(f)

def load_all_backup():
    if not os.path.exists(BACKUP_DATA):
        return {}
    with open(BACKUP_DATA, "r") as f:
        return json.load(f)

def load_all_admin():
    if not os.path.exists(ADMIN_RULE):
        return {}
    with open(ADMIN_RULE, "r") as f:
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

def save_all_fine(data):
    with open(FINE_DATA, "w") as f:
        json.dump(data, f, indent=4)

def save_all_backup(data):
    with open(BACKUP_DATA, "a") as f:
        json.dump(data, f, indent=4)

def save_all_admin(data):
    with open(ADMIN_RULE, "w") as f:
        json.dump(data, f, indent=4)


class Admin():
    # max_issue_days = 7
    admin_rule = load_all_admin()
    max_issue_days = admin_rule['max_issue_days']
    fine_rate = admin_rule['fine_rate']
    student_book = admin_rule['student_book']
    teacher_book = admin_rule['teacher_book']
    external_book = admin_rule['external_book']
    def __init__(self):
        pass

    @classmethod
    def view_system_total(self):
        book_data = load_all_data()
        member_data = load_all_member()
        issue_data = load_all_issue()
        fine_data = load_all_fine()
        total_books = 0
        available_books = 0

        for bid,b in book_data.items():
            total_books += b['total copies']
            available_books += b['available copies']


        print("="*30)
        print("Books Data : ")
        print(f"Total number of books : {total_books} ")
        print(f"Total number of Available Books: {available_books}")
        print(f"Total number of issued Books : {total_books - available_books}")
        print("="*30)


        member_count = 0
        active_member = 0
        # deactive_member = 0
        for mid,m in member_data.items():
            member_count +=1
            if m["status"] == "Active":
                active_member += 1


        # print("="*30)
        print("Books Data : ")
        print(f"Total number of Member : {member_count} ")
        print(f"Total number of Active Member: {active_member}")
        print(f"Total number of Deactive Member : {member_count - active_member}")
        print("="*30)


        print("Issued Book : ")

        book_id = []
        for iid , i in issue_data.items():
            if i['status'] == "Issued":
                book_id.append(i['book'])


        if book_id:
            for b in book_id:
                if b in book_data:
                    print(f"""
                        Book name : {book_data[b]['title']}
                        Available Copies : {book_data[b]['available copies']}
                        Total Copies : {book_data[b]['total copies']}
                    """ )
        else:
            print("No book is currently issued")
            print()
        print("="*30)
        print("Total Fine Collected : ")
        
        fine_amount = 0
        fine_pending = 0
        for fin, f in fine_data.items():
            if f['status'] == "Paid":
                fine_amount += f['amount']
            else:
                fine_pending += f['amount']

        print(f"Total Fine Collect is : {fine_amount}")
        print(f"Total Pending Fine : {fine_pending}")

        print("="*30)


    @classmethod
    def backup_data(self, backup_folder="backups"):
        file_list = [FILE_NAME , MEMBER_DATA, ISSUE_DATA, FINE_DATA, ADMIN_RULE]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(backup_folder, exist_ok=True)
        zip_name = os.path.join(backup_folder, f"json_backup_{timestamp}.zip")

        # Initialize the ZIP archive
        with zipfile.ZipFile(zip_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            for file in file_list:
                if os.path.exists(file):
                    # Add file to ZIP; arcname=os.path.basename(file) avoids nested folders
                    zf.write(file, arcname=os.path.basename(file))
                    print(f"Added: {file}")
                else:
                    print(f"Warning: {file} not found.")
        
        print(f"Backup saved to: {zip_name}")

    @classmethod
    def change_max_issue_days(self):
        # admin_rule = load_all_admin()
        # max_issue_days = admin_rue['max_issue_days']
        print(f"Current max issue days for a book is : {Admin.max_issue_days}")
        new_days = int(input("Enter new days you want to set : "))
        Admin.max_issue_days = new_days
        self.admin_rule['max_issue_days'] = new_days

        print(f"New max issue days is {Admin.max_issue_days}")

        save_all_admin(self.admin_rule)

    @classmethod
    def change_fine_rate(self):
        # admin_rule = load_all_admin()
        # max_issue_days = admin_rue['max_issue_days']
        print(f"Current Fine Per day is : {Admin.fine_rate}")
        new_fine = int(input("Enter new Fine amount you want to charge per day : "))
        Admin.fine_rate = new_fine
        self.admin_rule['fine_rate'] = new_fine

        print(f"New Fine rate is {Admin.fine_rate}")

        save_all_admin(self.admin_rule)

    @classmethod
    def change_book_count(self):
        user_input = input("Enter the member type you want to change total books they can issue (Teacher / Student / External) : ")

        if user_input == "Teacher":
            print(f"Current no of books Teacher can issue at a time is : {self.teacher_book}")
            new_book = int(input("Enter new no of book Teacher can issue at a time : "))
            Admin.teacher_book = new_book
            self.admin_rule['teacher_book'] = new_book

            print(f"New no of books Teacher can issue at a time : {Admin.teacher_book}")

            save_all_admin(self.admin_rule)

        elif user_input == "Student":
            print(f"Current no of books Student can issue at a time is : {self.student_book}")
            new_book = int(input("Enter new no of book Student can issue at a time : "))
            Admin.student_book = new_book
            self.admin_rule['student_book'] = new_book

            print(f"New no of books Teacher can issue at a time : {Admin.student_book}")

            save_all_admin(self.admin_rule)
        
        elif user_input == "External":
            print(f"Current no of books External can issue at a time is : {self.external_book}")
            new_book = int(input("Enter new no of book External can issue at a time : "))
            Admin.external_book = new_book
            self.admin_rule['external_book'] = new_book

            print(f"New no of books Teacher can issue at a time : {Admin.external_book}")

            save_all_admin(self.admin_rule)
        else:
            print("Enter valid option : ")
        

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
        print()

        if book_id not in data:
            print(" Invalid ID")
            return

        book = data[book_id]

        print("Leave blank to keep old value")

        new_title = input("New title: ")
        new_author = input("New author: ")
        new_genre = input("New genre: ")
        new_total = input("New total copies: ")
        print()

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
        print()


    @classmethod
    def remove_book(cls):
        data = load_all_data()
        print()

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
        print()


    @classmethod
    def view_all_book(cls):
        data = load_all_data()

        if not data:
            print("No books available")
            print()

        for bid , b in data.items():
            print(f"""
            Book id : {bid}
            Book title : {b['title']}
            Book author : {b['author']} 
            Available Copies : {b['available copies']}
            """)
        print()

    @classmethod
    def view_available_books(cls):
        data = load_all_data()
        print()

        found = False
        for bid, b in data.items():
            if int(b["available copies"]) > 0:
                print(f"{bid} | {b['title']} ({b['available copies']} available)")
                found = True

        if not found:
            print(" No available books")
            print()

    @classmethod
    def view_books_genre(cls,genre):
        data = load_all_data()
        print()

        found = False
        for bid, b in data.items():
            if b['genre'].lower() == genre.lower():
                print(f"{bid} | {b['title']}")
                found = True

        if not found:
            print(" No available books")
            print()

    @classmethod
    def import_csv(cls):
        print()
        filename = input("Enter CSV file: ")

        if not os.path.exists(filename):
            print(" File not found")
            return

        data = load_all_data()

        with open(filename, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                duplicate = False
                for b in data.values():
                    if b["isbn no"] == row["isbn no"]:
                        duplicate = True
                        break

                if not duplicate:
                    book = Books(
                        row["title"],
                        row["author"],
                        row["genre"],
                        int(row["total copies"]),
                        int(row["available copies"]),
                        row["isbn no"],
                        int(row["publish year"]),
                        row["shelf"]
                    )

        print("CSV import done")
        print()


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
            "joining date":self.join_date.isoformat(),
            "exp date":self.exp_date.isoformat(),
            "status" : self.status,
            "issued no of books":0,
            "issued book name":[],
            "fine" : 0
        }

        save_all_member(data)

    @classmethod
    def remove_member(cls):
        data = load_all_member()
        print()
        if not data:
            print(" No member available")
            return

        member_id = input("Enter Member ID to remove: ")

        if member_id not in data:
            print(" Invalid Member ID")
            print()
            return

        data.pop(member_id)
        save_all_member(data)

        print(" Member removed")
        print()

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
        print()

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
        print()

    @classmethod
    def view_profile(self):
        member_data = load_all_member()
        member_id = input("Enter member ID to see member profile : ")
        print()
        if member_id not in member_data:
            print("Invalid ID")
            return

        member = member_data[member_id]
        
        print(f"""
        Member name : {member['name']}
        Member phone : {member['phone']}
        Member email : {member['email']}
        Member member type : {member['member type']}
        Member currently issued book : {member['issued no of books']}
        List of book issued by Member : {member['issued book name']}
        Member fine amount : {member['fine']}
        Member status : {member['status']}
        """)
        print()

    @classmethod
    def toggle_activate_deactivate(self):
        member_data = load_all_member()
        member_id = input("Enter member ID to Activate/Deactivate Member : ")
        print()
        if member_id not in member_data:
            print("Invalid ID")
            return
        
        member = member_data[member_id]

        if member['status'] == "Active" :
            print(f"Member Deactivattion Completed ")
            member['status'] = "Deactivate"

        else:
            print(f"Member Activation Completed ")
            member['status'] = "Active"

        save_all_member(member_data)
        print()



class Fine():
    def __init__(self,member_id,amount=0):
        self.fine_id = str(uuid.uuid4())[:8]    
        self.member_id = member_id
        self.status = "Pending"
        self.amount = amount
        self.save()

    def save(self):
        data = load_all_fine()

        data[self.fine_id] = {
            "fine_id":self.fine_id,
            "member_id": self.member_id,
            "status":self.status,
            "anooubt":self.amount
        }

        save_all_fine(data)

    @classmethod
    def view_all_fine(self):
        fine_data = load_all_fine()
        member_data = load_all_member()

        member_id = []
        for fin, f in fine_data.items():
            if f['status'] == "Pending":
                member_id.append(f['member_id'])

        if member_id:
            for m in member_id:
                if m in member_data:
                    print(f"""
                        Member name : {member_data[m]['name']}
                        Pending Fine : {member_data[m]['fine']}
                    """ )

        else:
            print("No fine pending")
        


    @classmethod
    def view_fine_member(self):
        # fine_data = load_all_fine()
        member_data = load_all_member()

        member_id = input("Enter member ID to Check Fine : ")
        if member_id not in member_data:
            print("Invalid ID")
            return

        member = member_data[member_id]
        if member['fine'] > 0:
            print(f"Pending fine for {member['name']} is {member['fine']}")
        else:
            print(f"No pending fine for {member['name']}")

    @classmethod
    def pay_fine_member(self):
        fine_data = load_all_fine()
        member_data = load_all_member()
        fine = []
        member_id = input("Enter member ID to pay fine : ")
        if member_id not in member_data:
            print("Invalid ID")
            return

        for fid,f in fine_data.items():
            if f['member_id'] == member_id:
                fine = f

        member = member_data[member_id]

        # print(fine)
        if fine["status"] == "Pending":
            fine["status"] = "Paid"
            fine["amount"] = member["fine"]
            member["fine"] = 0

        else:
            print(f"No due fine for {member['name']}")


        save_all_member(member_data)
        save_all_fine(fine_data)
        # member = member_data[member_id]
        # print(f"Pending fine for {member['name']} is {member['fine']}")

    @classmethod
    def fine_history_member(self):
        fine_data = load_all_fine()
        member_data = load_all_member()
        fine = None
        member_id = input("Enter member ID to see member fine histroy : ")
        if member_id not in member_data:
            print("Invalid ID")
            return

        for fid,f in fine_data.items():
            if f['member_id'] == member_id:
                fine = f

        if fine :
            print(f"{member_id} has {fine['status']} amount of {fine['amount']} ")
        else:
            print(f"{member_id} doesn't have any fine history")

        # member = member_data[member_id]

        # # print(fine)
        # if fine["status"] == "Pending":
        #     fine["status"] = "Paid"
        #     fine["amount"] = member["fine"]
        #     member["fine"] = 0

        # else:
        #     print(f"No due fine for {member['name']}")


        # save_all_member(member_data)
        # save_all_fine(fine_data)
        # member = member_data[member_id]
        # print(f"Pending fine for {member['name']} is {member['fine']}")



class Issue_Return(Admin):
    def __init__(self,book_id,member_id):
        self.issue_id = str(uuid.uuid4())[:8]    
        self.issue_date = datetime.now()
        self.due_date = datetime.now() + timedelta(days=Admin.max_issue_days)
        self.renewal = 0
        self.book_id = book_id
        self.member_id = member_id
        self.status = "Issued"
        self.save()


    @classmethod
    def issue_book(self):
        admin_rule=load_all_admin()
        student_book = admin_rule['student_book']
        teacher_book = admin_rule['teacher_book']
        external_book = admin_rule['external_book']
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

        if (member["issued no of books"] >= student_book and member["member type"] == "Student") or (member["issued no of books"] >= teacher_book and member["member type"] == "Teacher") or (member["issued no of books"] >= external_book and member["member type"] == "External"):
            print("You already issued all the books you can !! return 1 book to issue new book !")
            return

        elif member["status"] == "Deactivate":
            print("Your Status is deactivated. You can't issue book")
            return

        elif member["fine"] > 0 :
            print(f"You have unpaid fine of {member["fine"]} , pay the amount first to issue the book")
            return
        
        elif book["available copies"] <=0 :
            print(f"No copies available for the book {book["title"]}")
            return

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
            "issue_id":self.issue_id,
            "book":self.book_id,
            "member": self.member_id,
            "issue date": self.issue_date.isoformat(),
            "due date": self.due_date.isoformat(),
            "renewal":self.renewal,
            "status":self.status
        }

        save_all_issue(data)

    @classmethod
    def return_book_by_bookid(self):
        issue_data = load_all_issue()
        book_data = load_all_data()
        member_data = load_all_member()
        fine_data = load_all_fine()
        admin_rule = load_all_admin()
        is_issued = False
        is_member = False
        issue = None

        book_id = input("Enter book Id : ")

        for iid , i in issue_data.items():
            if i['book'] == book_id:
                is_issued = True
                issue = i

        member_id = input("Enter member id : ")

        for mid , m in issue_data.items():
            if m['member'] == member_id:
                is_member = True
                # member = m

        if is_issued and is_member:
            # print("Return Available")
            if issue["status"] == "Return":
                print(f"Book is already Returned ")
                return

            book = book_data[issue['book']]
            # print(book['title'])
            member = member_data[issue['member']]

            loaded_issue = datetime.fromisoformat(issue['issue date'])
            loaded_due = datetime.fromisoformat(issue['due date'])

            today = datetime.now()
            diff = today - loaded_due

            if diff.days > 0:
                fine = 0
                if diff.days > 0 and diff.days < 7:
                    fine = diff.days * admin_rule['fine_rate']
                elif diff.days > 7:
                    fine = diff.days * admin_rule['fine_rate_30']
                
                issue["status"] = "Return"
                book["available copies"] += 1
                member["issued no of books"] -=1
                member["issued book name"].remove(str(book['title']))
                member['fine'] += fine
                fine = Fine(member['member_id'],fine)

                save_all_data(book_data)
                save_all_member(member_data)
                save_all_issue(issue_data)

            else:
            #! Due date logic to pay fine is pending

                issue["status"] = "Return"
                book["available copies"] += 1
                member["issued no of books"] -=1
                # print(type(book['title']))
                # print(type(member["issued book name"]))
                member["issued book name"].remove(str(book['title']))

                save_all_data(book_data)
                save_all_member(member_data)
                save_all_issue(issue_data)

                print("Book has been successfully returned")
                print("Without fine ")

        else:
            print("Member does not issued this book")


    @classmethod
    def renew_book_by_bookid(self):
        issue_data = load_all_issue()
        book_data = load_all_data()
        member_data = load_all_member()
        is_issued = False
        is_member = False
        issue = None

        book_id = input("Enter book Id : ")

        for iid , i in issue_data.items():
            if i['book'] == book_id:
                is_issued = True
                issue = i

        member_id = input("Enter member id : ")

        for mid , m in issue_data.items():
            if m['member'] == member_id:
                is_member = True
                # member = m

        if is_issued and is_member:
            print("Return Available")
            book = book_data[issue['book']]
            # print(book['title'])
            member = member_data[issue['member']]


            if issue["status"] == "Return":
                print(f"Book is already Returned ")
                

            #! Due date logic to pay fine is pending

            elif issue["renewal"] >= 1:
                print("Already one time Renewed. Now you can not renew this book !")
                return

            issue["status"] = "Issued"
            issue["renewal"] +=1 
            issue["issue date"] = datetime.now().day
            issue["due date"] = (datetime.now() + timedelta(days=7)).day
            # book["available copies"] += 1
            # member["issued no of books"] -=1
            # print(type(book['title']))
            # print(type(member["issued book name"]))
            # member["issued book name"].remove(str(book['title']))

            save_all_data(book_data)
            save_all_member(member_data)
            save_all_issue(issue_data)

            print("Book Renewed")
            print()

        else:
            print("Member does not issued this book")
    
    @classmethod
    def view_all_issued(self):
        issue_data = load_all_issue()
        book_data = load_all_data()
        book_id = []
        for iid , i in issue_data.items():
            if i['status'] == "Issued":
                book_id.append(i['book'])


        if book_id:
            for b in book_id:
                if b in book_data:
                    print(f"""
                        Book name : {book_data[b]['title']}
                        Available Copies : {book_data[b]['available copies']}
                        Total Copies : {book_data[b]['total copies']}
                    """ )
        else:
            print("No book is currently issued")
            print()

    #! Logic for overdue book is pending
    @classmethod
    def view_overdue_books(self):
        issue_data = load_all_issue()
        book_data = load_all_data()
        count = 0 
        for iid, issue in issue_data.items():
            # print("Inside the loop")
            loaded_issue = datetime.fromisoformat(issue['issue date'])
            loaded_due = datetime.fromisoformat(issue['due date'])

            today = datetime.now()
            diff = today - loaded_due

            if diff.days > 0:
                book_id = issue["book"]
                book = book_data[book_id]

                print(f"{book["title"]} is due from {diff.days}")
                count += 1
        
        if count <= 1:
            print("No book is overdue")
  
        
class Report():
    def __init__(self):
        pass

    @classmethod
    def search_book(cls):
        book_data = load_all_data()

        book_id = input("Enter book Title / author / ISBN / genre : ")

        book = []
        for bid,b in book_data.items():
            if (b['title'] == book_id or b['author'] == book_id or b['isbn no'] == book_id or b['genre'] == book_id):
                book.append(b)

        if book:
            for b in book:
                print(f"""
                Book title : {b['title']}
                Book author : {b['author']}
                Book isbn no : {b['isbn no']}
                Book genre : {b['genre']}
                Book available copies : {b['available copies']}
                """)

        else:
            print(f"No book available for {book_id}")

    @classmethod
    def search_member(cls):
        member_data = load_all_member()

        member_id = input("Enter Member Name / ID / phone / email : ")

        member = []
        for mid,m in member_data.items():
            if (m['name'] == member_id or m['phone'] == member_id or m['member_id'] == member_id or m['email'] == member_id):
                member.append(m)

        if member:
            for m in member:
                print(f"""
                Member name : {m['name']}
                Member phone : {m['phone']}
                member email : {m['email']}
                member Currently issued book : {m['issued no of books']}
                """)

        else:
            print(f"No member available for {member_id}")
    

    @classmethod
    def book_never_issued(cls):
        book_data = load_all_data()
        issue_data = load_all_issue()

        books = []
        for bid, b in book_data.items():
            issued = True
            for iid , i in issue_data.items():
                if i['book'] == b['book_id']:
                    issued = False
            if issued:
                books.append(b)

        print("Books that are never issued : ")
        if books:
            for b in books:
                print(f"{b["title"]}")
        else:
            print("All books have been issued once")
        print()

    @classmethod
    def most_issued_books(cls):
        issue_data = load_all_issue()
        book_data = load_all_data()

        count = {}

        for i in issue_data.values():
            b_id = i['book']
            count[b_id] = count.get(b_id,0) + 1

        sorted_books = sorted(count.items(), key=lambda x: x[1], reverse=True)[:5]

        print("\nTop 5 Most Issued Books:\n")
        for bid, c in sorted_books:
            if bid in book_data:
                print(f"{book_data[bid]['title']} -> Issued {c} times")

    @classmethod
    def highest_fine_member(cls):
        member_data = load_all_member()

        print("member_data")
        # print((member_data.values()))
        sorted_members = sorted(member_data.values() , key = lambda x:x['fine'],reverse = True)[:5]
        # print(sorted_members)
        print("\nTop Members with Highest Fines:\n")
        for m in sorted_members:
            print(f"{m['name']} -> {m['fine']}")

    @classmethod
    def monthly_issue_report(cls):
        issue_data = load_all_issue()

        month = int(input("Enter month (1-12): "))
        count = 0

        for i in issue_data.values():
            issue_date = datetime.fromisoformat(i['issue date'])
            if issue_date.month == month:
                count += 1

        print(f"Total books issued in month {month}: {count}")

    @classmethod
    def overdue_report(cls):
        issue_data = load_all_issue()
        book_data = load_all_book()

        print(" Overdue Book Reports : ")

        not_due = True

        for i in issue_data.value():
            if i['status'] == "Issued":
                due = datetime.fromisoformat(i['due date'])
                today = datetime.now()

                if today > due:
                    days = (today - due).days
                    book = book_data[i['book']]
                    print(f"{book['title']} -> Overdue by {days} days")
                    not_due = False

        if not_due:
            print("There is no overdue book ")
        print()


#--------------Main Menu---------------------

while True:
    print()
    print('-'*25)
    print("1. Book Management")
    print("2. Member Management")
    print("3. Issue & Return")
    print("4. Fine & Payments")
    print("5. Reports & Search")
    print("6. Admin Settings")
    print("0. Exit")
    print('-'*25)
    print()

    choice = int(input("Enter your Choice : "))

    #! book managment system
    if choice == 1:
        while True:        
            print()
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
            print()

            book_ch = int(input("Enter your Choice : "))

            if book_ch == 1:
                print('-'*25)
                print()

                print("Enter following book details : ")
                title = input("Enter title : ")
                author = input("Enter author : ")
                genre = input("Enter genre : ")
                total_copies = int(input("Enter total copies : "))
                available_copies = int(input("Enter available copies : "))
                isbn_no = int(input("Enter isbn no : "))
                publication_year = int(input("Enter publication year : "))
                shelf = input("Enter shelf location : ")
                print()
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
                Books.import_csv()
                
            elif book_ch == 8:
                break

            else:
                print("Select valid option")
            
    #! Member managment system

    elif choice == 2:
        while True:
            print()
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
            print()

            member_ch = int(input("Enter your choice : "))
            
            if member_ch == 1:
                print()
                print('-'*25)
                print("Enter following  details : ")
                name = input("Enter Name : ")
                phone = input("Enter phone : ")
                email = input("Enter email : ")
                member_type = input("Enter member type(Student/ Teacher / External) : ")
                print('-'*25)
                print()

                member1 = Member(name,phone,email,member_type)

            elif member_ch == 2:
                Member.remove_member()

            elif member_ch == 3:
                Member.update_member()

            elif member_ch == 4:
                Member.view_all_member()

            elif member_ch == 5:
                Member.view_profile()

            elif member_ch == 6:
                Member.toggle_activate_deactivate()

            elif member_ch == 7:
                break

            else:
                print("Enter valid choice : ")

    #!Issue menu

    elif choice == 3:
        while True:
            print()
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
            print()

            issue_ch = int(input("Enter your choice : "))
            
            if issue_ch == 1:
                Issue_Return.issue_book()

            elif issue_ch == 2:
                Issue_Return.return_book_by_bookid()
                
            elif issue_ch == 3:
                Issue_Return.renew_book_by_bookid()
            elif issue_ch == 4:
                Issue_Return.view_all_issued()

            elif issue_ch == 5:
                Issue_Return.view_overdue_books()
            elif issue_ch == 6:
                break
            else:
                print("Enter Valid Choice : ")

    #! Fine menu
    elif choice == 4:
        while True:
            print()
            print('-'*25)
            print("1.  Check fine for a member",
                  "2. Pay fine",
                  "3. View all pending fines",
                  "4. Fine history of a member",
                  "5. Back",
                    sep="\n"
                    )
            print('-'*25)
            print()

            fine_ch = int(input("Enter your choice : "))
            
            if fine_ch == 1:
                Fine.view_fine_member()
            elif fine_ch == 2:
                Fine.pay_fine_member()
            elif fine_ch == 3:
                Fine.view_all_fine()
            elif fine_ch == 4:
                Fine.fine_history_member()
            elif fine_ch == 5:
                break
            else:
                print("Select Valid option : dd")

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
                Report.search_book()
            
            elif report_ch == 2:
                Report.search_member()
            elif report_ch == 3:
                Report.most_issued_books()
            elif report_ch == 4:
                Report.highest_fine_member()
            elif report_ch == 5:
                Report.book_never_issued()
            elif report_ch == 6:
                Report.monthly_issue_report()
            elif report_ch == 7:
                Report.overdue_report()

            elif report_ch == 8:
                break

            else:
                print("Select valid option")

    #! Admin menu
    elif choice == 6:
        while True:
            print()
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
            print()

            admin_ch = int(input("Enter your choice : "))
            
            if admin_ch == 1:
                Admin.change_fine_rate()
            
            elif admin_ch == 2:
                Admin.change_max_issue_days()

            elif admin_ch == 3:
                Admin.change_book_count()

            elif admin_ch == 4:
                Admin.view_system_total()

            elif admin_ch == 5:
                Admin.backup_data()

            elif admin_ch == 6:
                break
            else:
                print("Select Valid option ")


    elif choice == 0:
        break

    else:
        print("Enter Valid option")
