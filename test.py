@classmethod
    def return_book_by_bookid(self):
        issue_data = load_all_issue()
        book_data = load_all_data()
        member_data = load_all_member()
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

        else:
            print("Member does not issued this book")