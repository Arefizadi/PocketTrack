expenses=[]
def add_expense():
    print("--- add expense ---")

    title = input("add expense title : ")
    if title=="":
        print("title must not be empty ")
        return 
    
    catagury = input("add expense catagury : ")
    if catagury=="":
        print("catagury must not be empty")
        return 

    try:
        amount = float(input("amount : "))
        if amount <= 0:
            print("amount must greater than zero")
            return 
    except ValueError:
        print("please enter valid numbre")
        return 
    expense={"Title":title,"Catagury":catagury,"Amount":amount}
    return expense

def show_all_expenses(expenses):
    number=1
    for expense in expenses:
        print("expense #",number)
        print("Title : ",expense["Title"])
        print("Catagury : ",expense["Catagury"])
        print("Amount",expense["Amount"])

        number=number+1

   
def show_total_expenses(expenses):
    total=0
    for expense in expenses:
        print("Amount",expense["Amount"])
        total=total+(expense["Amount"])
    print("All eexpenses you paid is : ",total)

def Category_summery(expenses):
     print("\n--- Category Summary ---")
     if len(expenses) == 0:
        print("No expenses recorded.")
        return

     category_totals = {}

     for expense in expenses:
        categury = expense["Catagury"]
        amount = expense["Amount"]

        category_totals[categury] = (
            category_totals.get(categury, 0) + amount 
            #dictionary.get(key, default_value)
        )

     for category, total in category_totals.items():
        print(category, ":", total)

def  Search_expense():
     if len(expenses) == 0:
        print("No expenses recorded.")
        return

     title = input("Enter expense title to search: ")
     found = False

     for expense in expenses:
        if expense["Title"] == title:
            print("\nExpense found!")
            print("Title:", expense["Title"])
            print("Category:", expense["Catagury"])
            print("Amount:", expense["Amount"])
            
def Delete_expense():
    show_all_expenses(expenses)
    if expenses=="":
        return 
        print("category list is empty ")
    try:
        expense_number=int(input("Please enter youer expense number : "))
        if expense_number<1 or expense_number>len(expenses):
            print("please enter number greater than 1 or ecual to ",len(expenses))
    except ValueError:
        print("please enter valid number")
        return     
    deleted_expense=expenses.pop(expense_number -1)
    print("you deleted ",deleted_expense["Title"])

while True:

    print("\n==============================")
    print("     Packet Track")
    print("==============================")
    print("1- Add expense")
    print("2- Show all expenses")
    print("3- Show total expenses")
    print("4- Category summery")
    print("5- Search expense")
    print("6- Delete expense")
    print("7- Exit")


    choose=input("choose a number 1-7")
    if choose == "1":
        new=add_expense()
        expenses.append(new)
        print("youer expense added secsesfully")

    elif choose =="2":
        show_all_expenses(expenses)

    elif choose =="3":
        show_total_expenses(expenses)
    elif choose =="4":
        Category_summery(expenses)
    elif choose =="5":
        Search_expense()
    elif choose =="6":
        Delete_expense()
    elif choose =="7":
        print("Thank you for using (pocket track)")
        break
    else:
        print("you must enter a number between 1 and 7")