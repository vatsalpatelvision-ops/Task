#Create a menu of operation for the list and dict

def main_menu():
    print()
    print("Select the data type ")
    print("Enter 1 for List ")
    print("Enter 2 for Dictionary ")
    print("Enter 3 for exit ")
    print()


def list_choice():
    """Menu for list opration"""
    print()
    print("Select the operation you want to perform : ")
    print("Enter 1 for append (add value at the end of list) ")
    print("Enter 2 for insert value at a particular index ")
    print("Enter 3 for pop element(Remove the last element) ")
    print("Enter 4 for updating value on a particular index ")
    print("Enter 5 for exit ")
    print()

def list_append():
    """Append element in list"""
    last_ele = int(input("Enter a number to add at the end of list : "))
    li.append(last_ele)
    print(f"Updated list : {li}")


def insert_list():
    """Inserting element in list"""
    index = int(input("Enter index on which you want to enter value : "))
    val = int(input("Enter the number you want to add on that index : "))
    if index > length_of_list:
        print("Index Out Of Bound")
    else : 
        li.insert(index , val)
        print(f"Updated list : {li}")

def pop_list():
    """Poping the element from the list"""
    try:
        print("Deleting last element from the list")
        li.pop()
        print(f"Updated list : {li}")
    except IndexError:
        print("Error : The list is empty ! Nothing to pop")

def update_list():
    """Updating the value in list"""
    index = int(input("Enter index on which you want to enter value : "))
    val = int(input("Enter the number you want to update on that index : "))
    try:
        li[index] = val
        print(f"Updated list : {li}")
    except IndexError:
        print("Error: Index is out of range.")


def dict_choice():
    print()
    print("Select the operation you want to perform : ")
    print("Enter 1 for retrive value using keys ")
    print("Enter 2 for delete specific key ")
    print("Enter 3 for updating the value of a key ")
    print("Enter 4 for clearing the entire dict  ")
    print("Enter 5 for exit ")
    print()


def search_key_dict():
    """Search value using the key in dict"""
    key = input("Enter the key you want to find out : ")
    try:
        print(user_dict[key])
    except KeyError:
        print(f"Error : the key {key} does not exist.")

def delete_using_key():
    """Delete using key"""
    try:
        key = input("Enter the key to delete it from the dict : ")
        user_dict.pop(key)
        print(f"Your Dict : {user_dict}")
    except KeyError:
        print(f"Error : the key {key} does not exist.")

def update_using_key():
    """update using key"""
    try:
        key = input("Enter the key to update it's value : ")
        val = input("Enter the value you want to update : ")
        value_type = input("Enter value type (str/int/float): ")
        if value_type == "int":
            user_dict[key] = int(val)
        elif value_type == "float":
            user_dict[key] = float(raw_value)
        else:
            user_dict[key] = raw_value

        # user_dict.update({key:val})
        print(f"Your Dict : {user_dict}")
    except KeyError:
        print(f"Error : the key {key} does not exist.")


def clear_dict():
    """Clear the entire dict"""
    print("Clearning the Dict ")
    user_dict.clear()
    print(f"Your Dict : {user_dict}")


print("Hello User !!")
ch = ""
list_ch = ""
dict_ch = ""

while ch!= "3":
    main_menu()
    ch = input("Enter Your Choice : ").strip()
    print()

    if ch == "1":

        num =  int(input("How many elements you want to enter : "))
        
        print(f"You want to enter {num} element in list")

        # li = list(map(int, input("Enter numbers separated by space: ").split()))
        li = list(eval(input("Enter a list separated by comma (For string use quotes): ")))
        print("List:", li)
        length_of_list= len(li)


        # User menu for the list
        while list_ch != "5" : 
            list_choice()

            list_ch =  input("Enter your Choice : ").strip()
            
            if list_ch == "1":
                list_append()


            elif list_ch == "2":
                insert_list()

            elif list_ch == "3":
                pop_list()
                
            elif list_ch == "4":
                update_list()

            else:
                print("Select Valid Option")


    elif ch == "2":
        n = int(input("Enter the number of entries: "))
        user_dict = {}
        for _ in range(n):
            key = input("Enter key: ")
            
            value_type = input("Enter value type (str/int/float): ")
            raw_value = input("Enter value: ")

            if value_type == "int":
                user_dict[key] = int(raw_value)
            elif value_type == "float":
                user_dict[key] = float(raw_value)
            else:
                user_dict[key] = raw_value

            # user_dict[key] = raw_value
        print(f"Your Dict : {user_dict}")



        while dict_ch != "5" : 
            dict_choice()

            dict_ch =  input("Enter your Choice : ").strip()

            if dict_ch == "1":
                
                search_key_dict()

            elif dict_ch == "2":
                
                delete_using_key()

            elif dict_ch == "3":
                
                update_using_key()

            elif dict_ch == "4":
                
                clear_dict()
            
            else :
                print("Select valid option")


    else:
        print("Select Valid Option")
   