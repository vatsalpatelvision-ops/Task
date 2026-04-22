
class Report():

    @classmethod
    def highest_fine_members(cls):
        # Purpose: Display top members with highest fines
        member_data = load_all_member()

        sorted_members = sorted(member_data.values(), key=lambda x: x['fine'], reverse=True)[:5]

        print("\nTop Members with Highest Fines:\n")
        for m in sorted_members:
            print(f"{m['name']} -> {m['fine']}")

    @classmethod
    def monthly_issue_report(cls):
        pass

    @classmethod
    def overdue_report(cls):
        # Purpose: Show all overdue books with delay in days
        issue_data = load_all_issue()
        book_data = load_all_data()

        print("\nOverdue Books Report:\n")

        for i in issue_data.values():
            if i['status'] == "Issued":
                due = datetime.fromisoformat(i['due date'])
                today = datetime.now()

                if today > due:
                    days = (today - due).days
                    book = book_data[i['book']]
                    print(f"{book['title']} -> Overdue by {days} days")


# =========================================================
# 2. ISSUE VALIDATION FUNCTION
# Purpose: Add missing rules (membership expiry and due warning)
# =========================================================

def extra_issue_validations(member, member_id):
    # Check if membership is expired
    exp = datetime.fromisoformat(member['exp date'])
    if datetime.now() > exp:
        print("Membership expired. Cannot issue book.")
        return False

    # Warn if any issued book is due within 2 days
    for i in load_all_issue().values():
        if i['member'] == member_id and i['status'] == "Issued":
            due = datetime.fromisoformat(i['due date'])
            if 0 <= (due - datetime.now()).days <= 2:
                print("Warning: You have books due within 2 days.")

    return True

# Usage:
# Inside Issue_Return.issue_book():
# if not extra_issue_validations(member, member_id):
#     return


# =========================================================
# 3. BLOCK DELETE IF BOOK IS ISSUED
# Purpose: Prevent deletion of books currently issued
# =========================================================

def block_delete_if_issued(book_id):
    issue_data = load_all_issue()

    for i in issue_data.values():
        if i['book'] == book_id and i['status'] == "Issued":
            print("Cannot delete book. It is currently issued.")
            return False

    return True

# Usage:
# Inside Books.remove_book():
# if not block_delete_if_issued(book_id):
#     return


# =========================================================
# 4. LOST BOOK FUNCTION (Add inside Issue_Return class)
# Purpose: Handle lost book scenario with fixed fine
# =========================================================

class Issue_Return():

    @classmethod
    def lost_book(cls):
        member_data = load_all_member()
        book_data = load_all_data()

        member_id = input("Enter member ID: ")
        book_id = input("Enter lost book ID: ")

        if member_id not in member_data or book_id not in book_data:
            print("Invalid ID")
            return

        member = member_data[member_id]
        book = book_data[book_id]

        fine_amount = 500

        if book['title'] in member['issued book name']:
            member['issued book name'].remove(book['title'])
            member['issued no of books'] -= 1
            member['fine'] += fine_amount

            Fine(member_id, fine_amount)

            print(f"Lost book fine {fine_amount} added")

            save_all_member(member_data)
        else:
            print("Member does not have this book")


# =========================================================
# 5. PAYMENT RECEIPT FUNCTION
# Purpose: Show receipt after fine payment
# =========================================================

def print_receipt(member, fine):
    print("\n===== PAYMENT RECEIPT =====")
    print(f"Member: {member['name']}")
    print(f"Amount Paid: {fine['amount']}")
    print("Status: SUCCESS")
    print("==========================\n")

# Usage:
# Call inside Fine.pay_fine_member() after updating data


# =========================================================
# 6. SAFE LIST REMOVE
# Purpose: Prevent crash if item not found in list
# =========================================================

def safe_remove(lst, item):
    if item in lst:
        lst.remove(item)


# =========================================================
# 7. MENU UPDATES
# Purpose: Connect new functions to menu system
# =========================================================

# Replace inside Reports menu:

"""
elif report_ch == 3:
    Report.most_issued_books()

elif report_ch == 4:
    Report.highest_fine_members()

elif report_ch == 6:
    Report.monthly_issue_report()

elif report_ch == 7:
    Report.overdue_report()
"""


# Replace Issue menu display:

"""
print("1. Issue book to member",
      "2. Return book",
      "3. Renew book",
      "4. View all issued books",
      "5. View overdue books",
      "6. Lost book",
      "7. Back", sep="\\n")
"""

# Add logic:

"""
elif issue_ch == 6:
    Issue_Return.lost_book()

elif issue_ch == 7:
    break
"""
