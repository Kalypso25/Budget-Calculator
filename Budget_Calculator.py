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
    print("10.Exit")
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

    _greeting = input("Enter 'v' to view your opening balances or 'm' for main menu: ").lower()

    if _greeting in ["v"]:  # displays balances
        calculate_totals()
        menu_items()

    if _greeting in ["m"]: #returns to main menu
        print("Opening Main menu")
        menu_items()
    elif _greeting not in ["v", "m"]:  # accepts invalid inputs
        print("Invalid entry")
        retry = input("Please enter 'v' to view your opening balances or 'm' for the main menu").lower()
        if _greeting in ["v"]:
            calculate_totals()
            main_menu = input("Open main menu? (y/n)").lower()
            if main_menu in ["y", "yes"]:
                menu_items()
            elif main_menu in ["n", "no"]:
                print("Returning to main menu")
                menu_items()

    if _greeting in ["m"]:  # main menu
        print("Opening Main menu")
        menu_items()

def addExp (expenses): #option 1
    add_exp = input("Do you have an expense to add (y/n)? ").lower()
    if add_exp in ["y", "yes"]:
        expNam = input("Please add the name of your expense: ")
        expValue = float(input("Please add your expense cost (no commas or special characters): "))
        expenses[expNam] = expValue
        user_confirm = input(f"Confirm expense: {expNam} for ${expValue}? (y/n): ").lower() #validation
        if user_confirm in ["y", "yes"]:
            print("Expense saved successfully! ")
            more_Expenses = input("Do you have another expense to add? (y/n) ").lower()
            if more_Expenses in ["y", "yes"]:
                expNam = input("Please add the name of your expense: ")
                expValue = float(input("Please add your expense cost (no commas or special characters): "))
                expenses[expNam] = expValue
                user_confirm2 = input(f"Confirm expense: {expNam} for ${expValue}? (y/n): ").lower()  # validation
                if user_confirm2 in ["y", "yes"]:
                        print("Expense saved successfully! ")
            elif more_Expenses in ["n","no"]:
                return
        else: # checks for invalid entries
            print("Invalid entry!")
            retry = input("Please enter ('r') to retry or ('m') for the main menu: ").lower()
            if retry == "r":
                expNam = input("Please add the name of your expense: ")
                expValue = float(input("Please add your expense cost (no commas or special characters): $"))
                expenses[expNam] = expValue
                user_confirm = input(f"Confirm expense: {expNam} for ${expValue}? (y/n): ").lower()  # validation
                if user_confirm in ["y", "yes"]:
                    print("Expense saved successfully! ")
                    more_Expenses = input("Do you have another expense to add? (y/n) ").lower()
                    more_Expenses in ["y", "yes"]
                    expNam = input("Please add the name of your expense: ")
                    expValue = float(input("Please add your expense cost (no commas or special characters): "))
                    expenses[expNam] = expValue
                    user_confirm = input(f"Confirm expense: {expNam} for ${expValue}? (y/n): ").lower()  # validation
                    if more_Expenses in ["n","no"]:
                        return
                    if user_confirm in ["y", "yes"]:
                        print("Expense saved successfully! ")
            elif retry == "m":
                return
    elif add_exp in ["n", "no"]:
        print("There are no expenses to add.")
        print("Returning to Main Menu.")
        return

def viewExp(expenses): #option 2
    if not expenses: #checks for empty dictionary
        print("No expenses to display!")
        return
    print(f"Here are your current expenses: ")
    for index, (key, value) in enumerate(expenses.items(), start=1):
        print(f"{index}. {key}: ${value:.2f}")
        print()

def viewIncome(income): #option 5 #displays income and checks for empty dictionary
    if not income:
        print("There is currently no income listed!")
        return
    print(f"Here is your total income: ")
    for index, (key,value) in enumerate(income.items(), start=1):
        print(f"{index}. {key}: ${value:.2f}")
        print()

def viewSavings(savings): #option 9
    if not savings:
        print("There is not savings to display!")
        return
    print(f"Here is your total savings: ")
    for index, (key,value) in enumerate(savings.items(), start=1): #numbers entries starting at index 1
        print(f"{index}. {key}: ${value:.2f}")
        print()

def removeExp(expenses): #option 3
    expense_list = list(expenses.keys())
    remove_Exp = input("Would you like to remove an expense (y/n)? ").lower()
    if remove_Exp in ["y", "yes"]:
        viewExp(expenses)
        user_choice = int(input("Which expense would you like to remove? "))
        if user_choice >= 1 and user_choice <= len(expense_list):  # validation
            expenses_to_remove = expense_list[user_choice - 1]
            del expenses[expenses_to_remove]
            print("Expense removed successfully! ")
            remove_more = input("Would you like to remove another entry (y/n)? ").lower()
            if remove_more in ["y", "yes"]:
                removeExp(expenses)
            elif remove_more in ["n", "no"]:
                print("Returning to Main Menu.")
        else: # checks for invalid entries
            print("Invalid Choice! Please enter a number between 1 and", len(expense_list))
    elif remove_Exp in ["n", "no"]:
        print("Returning to Main Menu.")
        return #exit the function, loop will show menu automatically
    else: # checks for invalid entries
        print("Invalid entry. Returning to Main Menu. ")
        return #exit the function, loop will show menu automatically

def addIncome(income): #option 4
    income_list = list(income.keys()) #dictionary to list for indexing
    add_Income = input("Would you like to add income (y/n)? ").lower()
    if add_Income in ["y", "yes"]:
        viewIncome(income)
        incomeName = input("What is the name of your income: ").title()
        incomeValue = float(input("How much is your income (no commas or special characters): "))
        incomeValue = float(f"{incomeValue:.2f}")
        income[incomeName] = incomeValue
        user_confirm = input(f"Confirm income: {incomeName} for ${incomeValue}? (y/n): ").lower()  # validation

        if user_confirm in ["y", "yes"]:
            print("Income saved successfully! ")
        else:  # invalid entries
            print("Invalid entry!")
            retry = input("Please enter ('r') to retry or ('m') for the main menu").lower()
            if retry == "r":
                incomeName = input("What is the name of your income: ").title()
                incomeValue = float(input("How much is your income (no commas or special characters): "))
                incomeValue = float(f"{incomeValue:.2f}")
                income[incomeName] = incomeValue
            elif retry == "m":
                return
    elif add_Income in ["n", "no"]:
        print("There is no income to add.")
        print("Returning to Main Menu.")
        return


def removeIncome(income): #option 6 Allows user to remove income
    income_list = list(income.keys())
    remove_income = input("Would you like to remove income (y/n)? ").lower()
    if remove_income in ["y", "yes"]:
        viewIncome(income)
        user_choice = int(input("Which income would you like to remove? "))
        if user_choice >= 1 and user_choice <= len(income_list):  # validation
            income_to_remove = income_list[user_choice - 1]
            del income[income_to_remove]
            print("Expense removed successfully! ")
            remove_more = input("Would you like to remove another entry (y/n)? ").lower()
            if remove_more in ["y", "yes"]:
                removeIncome(income)
            elif remove_more in ["n", "no"]:
                print("Returning to Main Menu.")
        else: # checks for invalid entries
            print("Invalid Choice! Please enter a number between 1 and", len(income_list))
    elif remove_income in ["n", "no"]:
        print("Returning to Main Menu.")
        return #exit the function, loop will show menu automatically
    else: # checks for invalid entries
        print("Invalid entry. Returning to Main Menu. ")
        return #exit the function, loop will show menu automatically

def addSavings(savings): #option 7 Allows users to add money to savings
    add_savings = input("Do you have savings to add (y/n)? ").lower()
    if add_savings == "y" or add_savings == "yes":
        savingsNam = input("Please add the name of your savings goal: ")
        savingsValue = float(input("Please enter the amount for savings goal (no commas or special characters): "))
        savings[savingsNam] = savingsValue
        user_confirm = input(f"Confirm savings: {savingsNam} for ${savingsValue}? (y/n): ").lower()  # validation
        if user_confirm == "y" or user_confirm == "yes": #validation
            print("Savings successfully added! ")
        else:  # invalid entries
            print("Invalid entry!")
            retry = input("Please enter ('r') to retry or ('m') for the main menu").lower()
            if retry == "r":
                savingsNam = input("Please add the name of your savings goal: ")
                savingsValue = float(input("Please enter the amount for savings goal (no commas or special characters): "))
                savingsValue = float(f"{savingsValue:.2f}")
                savings[savingsNam] = savingsValue
            elif retry == "m":
                return
    elif add_savings in ["n", "no"]:
        print("There is no savings to add.")
        print("Returning to Main Menu.")
        return

def removeSavings(savings): #option 8 Allows users to withdraw money from savings goal
    savings_list = list(savings.keys())
    remove_savings = input("Would you like to remove money from savings (y/n)? ").lower()
    if remove_savings in ["y", "yes"]:
        viewSavings(savings)
        user_choice = int(input("Which savings goal would you like to withdraw from: "))
        if user_choice >=1 and user_choice <= len(savings_list):
            savings_2_remove = savings_list[user_choice -1 ] #browse by index to select savings goal
            remove_value = float(input(f"How much would you like to remove from {savings_2_remove} (no commas or special characters):"))
            confirm_removal = input(f"Confirm savings deduction: ${remove_value} (y/n)? ").lower()
            if confirm_removal == "y" or confirm_removal == "yes":
                print("Savings successfully removed!")
                user_amount = savings[savings_2_remove]  # current value stored in selected entry
                if remove_value <= user_amount: # Check if they have enough
                    savings[savings_2_remove] -= remove_value  # Subtract from the goal
                    print(f"Withdrawal successful! New balance in {savings_2_remove}: ${savings[savings_2_remove]:.2f}")
                else:
                    print(f"Insufficient funds! You only have ${user_amount:.2f} in {savings_2_remove}")
            elif confirm_removal == "n" or confirm_removal == "no":
                return
        else: # checks for invalid entries
            print("Invalid choice! Please enter a number between 1 and", len(savings_list))
    elif remove_savings in ["n", "no"]:
        print("You selected no. Returning to main menu")
        return
    elif remove_savings not in ["n", "no", "y", "yes"]:
        print("Invalid entry! Returning to main menu")
        return


greeting()

while running:
    menu_items()
    user_choice = (input("Select an option from main menu: "))
    if user_choice == "1":
        addExp(expenses)
    elif user_choice == "2":
        viewExp(expenses)
    elif user_choice == "3":
        removeExp(expenses)
    elif user_choice == "4":
        addIncome(income)
    elif user_choice == "5":
        viewIncome(income)
    elif user_choice == "6":
        removeIncome(income)
    elif user_choice == "7":
        addSavings(savings)
    elif user_choice == "8":
        removeSavings(savings)
    elif user_choice == "9":
        viewSavings(savings)
    elif user_choice == "10":
        print("Thank you for using our budgeting app. ")
        print("GoodBye!")
        running = False
    else:
        print("Invalid selection! Please choose 1-10")



