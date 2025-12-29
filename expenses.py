import datetime

FILE_NAME = "expenses.txt"

# Add an expense
def add_expense():
    date = datetime.date.today()
    category = input("Enter expense category (Food, Travel, Rent, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

    print("Expense added successfully!\n")

# View all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nDate        Category   Amount   Description")
            print("--------------------------------------------")
            for line in file:
                date, category, amount, description = line.strip().split(",")
                print(f"{date}   {category}   {amount}   {description}")
            print()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Calculate total expenses
def total_expenses():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, _, amount, _ = line.strip().split(",")
                total += float(amount)
        print(f"\nTotal Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Main menu
def main():
    while True:
        print("===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
main()