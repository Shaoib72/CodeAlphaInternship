import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        try:
            self.expenses = pd.read_csv(filename)
        except FileNotFoundError:
            self.expenses = pd.DataFrame(columns=["Description", "Category", "Amount", "Date"])
    
    def add_expense(self, description, category, amount, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        new_expense = pd.DataFrame([[description, category, amount, date]], columns=["Description", "Category", "Amount", "Date"])
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        self.save_expenses()
    
    def save_expenses(self):
        self.expenses.to_csv(self.filename, index=False)
    
    def view_expenses(self):
        return self.expenses
    
    def summarize_expenses(self):
        summary = self.expenses.groupby("Category")["Amount"].sum()
        total = self.expenses["Amount"].sum()
        return summary, total
    
    def get_insights(self):
        max_expense = self.expenses.loc[self.expenses["Amount"].idxmax()]
        most_frequent_category = self.expenses["Category"].mode()[0]
        return {
            "max_expense": max_expense,
            "most_frequent_category": most_frequent_category
        }

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Get Insights")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter description: ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            date = date if date else None
            tracker.add_expense(description, category, amount, date)
            print("Expense added successfully.")
        elif choice == '2':
            print("\nExpenses:")
            print(tracker.view_expenses())
        elif choice == '3':
            summary, total = tracker.summarize_expenses()
            print(f"\nTotal expenses: ${total:.2f}")
            print("Expenses by category:")
            print(summary)
        elif choice == '4':
            insights = tracker.get_insights()
            print(f"\nHighest expense: {insights['max_expense']['Description']} - ${insights['max_expense']['Amount']:.2f}")
            print(f"Most frequent category: {insights['most_frequent_category']}")
        elif choice == '5':
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
