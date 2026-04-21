




class Books():
    pass








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
                total_copies = input("Enter total copies : ")
                available_copies = input("Enter available copies : ")
                isbn_no = input("Enter isbn no : ")
                publication_year = input("Enter publication year : ")
                shelf = input("Enter shelf location : ")
                print('-'*25)

                book1 = Books(title, author, genre, total_copies, available_copies, isbn_no, publication_year, shelf)

            elif book_ch ==2:
                title = input("Enter the title to remove the book : ")
                data = load_all_data()
                if title in data:
                    # book_id = data[title]["bookid"]
                    # title = data[title]
                    author = data[title]["author"]
                    genre = data[title]["genre"]
                    total_cp = data[title]["total copies"]
                    available_cp = data[title]["available copies"]
                    isbn_no = data[title]["isbn no"]
                    publish_year = data[title]["publish year"]
                    shelf = data[title]["shelf"]
                    book1 = Books(title,author,genre,total_cp,available_cp,isbn_no,publish_year,shelf)

                    book1.remove_book(title)
                else:
                    print("No book exsits")
                

            elif book_ch == 4:
                
                Books.view_all_book()

            elif book_ch == 5:
                Books.view_available_books()

            elif book_ch == 6:
                genre = input("Enter the genre : ")
                Books.view_book_by_genre(genre)

            elif book_ch == 7:
                file_name = input("Enter the file name : ")
                # if not os.path.exists(file_name):
                #     return {}
                # with open(file_name, "r") as f:
                #     return json.load(f)
                original_data = load_all_data()
                data = load_file_enter(file_name)
                original_data.append(data)

                save_all_data(original_data)


            else:
                break
            


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
                pass
            else:
                break

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
                pass
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




    