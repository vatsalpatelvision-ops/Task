"""Library Managment system"""
import uuid
import os
import json

FILE_NAME = "book_data.json"


def load_all_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_all_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

class Books():
    def __init__(self, title, author, genre, total_cp, available_cp, isbn_no, publish_year, shelf):
        

        data = load_all_data()

        if title in data:
            print("Existing Book Found")
            self.author = data[title]["author"]
            self.genre = data[title]["genre"]
            self.total_cp = data[title]["total copies"]
            self.available_cp = data[title]["available copies"]
            self.isbn_no = data[title]["isbn no"]
            self.publish_year = data[title]["publish year"]
            self.shelf = data[title]["shelf"]
        else:
            self.book_id = str(uuid.uuid4())[:8]    
            print("New Book")
            self.title = title
            self.author = author
            self.genre = genre
            self.total_cp = total_cp
            self.available_cp = available_cp
            self.isbn_no = isbn_no
            self.publish_year = publish_year
            self.shelf = shelf
            self.save()



    def save(self):
        data = load_all_data()

        data[self.title] = {
            "bookid":self.book_id,
            "author": self.author,
            "genre": self.genre,
            "total copies": self.total_cp,
            "available copies":self.available_cp,
            "isbn no":self.isbn_no,
            "publish year":self.publish_year,
            "shelf":self.shelf
        }

        save_all_data(data)

    def remove_book(self):
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
                total_copies = input("Enter total copies : ")
                available_copies = input("Enter available copies : ")
                isbn_no = input("Enter isbn no : ")
                publication_year = input("Enter publication year : ")
                shelf = input("Enter shelf location : ")
                print('-'*25)

                book1 = Books(title, author, genre, total_copies, available_copies, isbn_no, publication_year, shelf)

            else:
                break
            

    else:
        break




    