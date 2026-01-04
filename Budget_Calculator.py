import time
"""
budget calc
"""
# establish constants
expenses = {}
income = {}
savings = {}
running = True
totalExp = 0 #initalization
totalSavings = 0 #initalization
totalIncome = 0 #initalization


#menu
def menu_items():
    print("==== Budget Calculator ====")
    print("1. Add Expense ")
    print("2. View Expenses ")
    print("3. Remove Expense")
    print("4. Add Income")
    print("5. View Income")
    print("6. Remove Income")
    print("7. Add Money to Savings")
    print("8. Remove Money From Savings")
    print("9. View Savings")
    print("10. Exit")
    print()


def calculate_totals():
    """ Calculate and return total expenses, income, and savings."""
    exp_value_totals = sum(expenses.values())
    savings_value_totals = sum(savings.values())
    income_value_totals = sum(income.values())
    print(f"Your opening expense balance is: {exp_value_totals:.2f} \n"
          f"Your total income is:  {income_value_totals:.2f} \n"
          f"Your total savings balance is: {savings_value_totals:.2f}")


def greeting():
    """Displays welcome message and opening balances. """
    print("\n" + "=" * 50)
    print("  WELCOME TO THE BUDGET CALCULATOR".center(50))
    print("=" * 50 + "\n")
    print("© 2026 Kalyspo25 | github.com/Kalypso25")
    print()

    _greeting = input("Enter 'v' to view your opening balances or 'm' for main menu: ").lower()

    if _greeting == "v":  # displays balances
        calculate_totals()
        print("Opening main menu..")
        menu_items()
    elif _greeting == "m": #returns to main menu
            print("Opening Main menu.")
            time.sleep(5) #allows user time to read output before returning to main menu
            menu_items()

    else:  # accepts invalid inputs
        print("Invalid entry. Returning to main menu. ")
        menu_items()

    
def more_items(data_dict, category_name):
    more_input = input("Do you have another entry to add? (y/n) ").lower()
    if more_input in ["y", "yes"]:
        entry(data_dict, category_name)
    elif more_input in ["n", "no"]:
        print(f"No entry added.\n Returning to main menu.")
    else:
        print("Invalid entry.")
        more_items(data_dict, category_name)

def entry(data_dict, category_name):
    item_Name = input(f"Add {category_name.lower()} name: ")
    item_Value = float(input(f"Add {category_name.lower()} amount (no commas or special characters): "))
    user_confirm = input(f"Confirm entry: {category_name.lower()}: {item_Name}? (y/n): ").lower() #validation
   
    if user_confirm in ["y", "yes"]:
        data_dict[item_Name] = item_Value
        print(f"{category_name} saved successfully! ")
        more_items(data_dict, category_name)

    elif user_confirm in ["n", "no"]:
        print("Entry not saved.")
        go_to_menu = input("Open main menu? (y/n)").lower()
        if go_to_menu in ["y", "yes"]:
            menu_items()
        elif go_to_menu in ["n", "no"]:
            more_items(data_dict, category_name)

def view_data(data_dict, category_name):
    """Displays any dictionary/ menu item"""
    if not data_dict:
        print(f"No {category_name.lower()} to display!")
        return
    elif data_dict:
        print(f"Here is your {category_name.lower()}")
        for index, (key,value) in enumerate(data_dict.items(), start=1):
            print(f"{index}. {key}: ${value:.2f}")
            time.sleep(3)

def remove_data(data_dict, category_name):
    if not data_dict:
        print(f"No {category_name.lower()} to display! ")
        return
    
    elif data_dict:
        print(f"Here is your {category_name.lower()}: ")
        for index, (key,value) in enumerate(data_dict.items(), start=1):
            print(f"{index}. {key}: ${value:.2f}")
            time.sleep(3)
    
    user_choice = int(input("Enter the item you want to remove: "))
    if user_choice >= 1 and user_choice <= len(data_dict):
        data_list = list(data_dict.keys())
        item_to_remove = data_list[user_choice -1] #get key at index
        del data_dict[item_to_remove]
        print(f" {item_to_remove} removed successfully!")
    
    else:
        print("Invalid choice!")


greeting()

while running:
    menu_items()
    user_choice = (input("Select an option from main menu: "))
    if user_choice == "1":
        entry(expenses,"Expense")
    elif user_choice == "2":
        view_data(expenses, "Expenses")
    elif user_choice == "3":
        remove_data(expenses, "Expenses")
    elif user_choice == "4":
        entry(income, "Income")
    elif user_choice == "5":
        view_data(income, "Income")
    elif user_choice == "6":
        remove_data(income, "Income")
    elif user_choice == "7":
        entry(savings, "Savings")
    elif user_choice == "8":
        remove_data(savings, "Savings")
    elif user_choice == "9":
        view_data(savings, "Savings")
    elif user_choice == "10":
        print("Thank you for using our budgeting app. ")
        print("GoodBye!")
        print("\n© 2026 Kalypso25 | github.com/Kalypso25")
        running = False
    else:
        print("Invalid selection! Please choose 1-10")
        time.sleep(2)
