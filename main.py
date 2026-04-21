import src.interface as ui
from datetime import datetime, date
import os
os.system("cls")

while True:

    start = int(input(ui.MAIN_MENU))

    if start == 1:

        while True:
            choice = int(input(ui.DATE_MENU))

            if choice == 1:
                dt = date.today()
                user_date = dt.strftime("%d/%m/%Y")
                
            elif choice == 2:
                user_date = str(input("Enter the date (DD/MM/YYYY): "))
                date_obj = datetime.strptime(user_date, "%d/%m/%Y")
                dt = date_obj.strftime("%Y-%m-%d")

            elif choice == 3:
                break

            else:
                print("\nInvalid action.")
                continue

            description = str(input("\nDescription: "))
            value = float(input("\nValue: $"))
            method = str(input(ui.PAYMENT_METHOD_MENU))

            if method == "1":
                method = "Debit/PIX"
            
            elif method == "2":
                method = "Credit"

            confirmation = int(input(f"\n{user_date}, {description}, ${value}, {method}" + ui.CONFIRMATION_MENU))

            if confirmation == 1:
                line = (f"{dt},{description},{value},{method}\n")

                with open("data/expenses.csv", "a", encoding="utf-8") as file:
                    file.write(line)
                
                print("\n\n\033[1;32mExpense saved successfully!\033[m")
                
                question = int(input(ui.REPEAT_EXPENSE_MENU))

                if question == 1:
                    continue
                
                else:
                    break

            else:
                continue
    
    elif start == 2:
        
        while True:
            choice = int(input(ui.MONTH_MENU))
            print()

            if choice >= 1 and choice <= 12:  
                with open("data/expenses.csv", "r", encoding="utf-8") as file:
                    lines = file.readlines()

                total = 0

                for line in lines:
                    parts = line.split(",")
                    value = float(parts[2])
                    date_str = parts[0]
                    dt = datetime.strptime(date_str, "%Y-%m-%d")
                    
                    if dt.month == choice:
                        print(line)

                        total = total + value

                print(f"\nTotal spent in the month: ${total}")
                
                question = int(input(ui.REPEAT_QUERY_MENU))

                if question == 1:
                    continue
                
                else:
                    break

            elif choice == 13:
                break

            else:
                print("Invalid option.")
                continue
    
    elif start == 3:
        
        choice = int(input(ui.DELETE_MENU))

        if choice >= 1 and choice <= 12:
            with open("data/expenses.csv", "r", encoding="utf-8") as file:
                lines = file.readlines()
                enumerate(lines)

            while True:
                
                month_lines = []
                
                for line in lines:
                    parts = line.split(",")
                    date_str = parts[0]
                    dt = datetime.strptime(date_str, "%Y-%m-%d")

                    if dt.month == choice:
                        month_lines.append(line)
                    
                
                for i in range(len(month_lines)):
                    print(f"\n{i + 1} - {month_lines[i]}")  
                
                delete_item = int(input("\nEnter the number of the expense you wish to delete: "))

                if delete_item >= 1 and delete_item <= len(month_lines):

                    confirmation = int(input(f"\n\n\033[1;31m{month_lines[delete_item - 1]}\033[m" + ui.DELETE_CONFIRMATION_MENU))

                    if confirmation == 1:
                        lines.remove(month_lines[delete_item - 1])
                        del month_lines[delete_item - 1]

                        with open("data/expenses.csv", "w", encoding="utf-8") as file:
                            file.writelines(lines)

                        print("\n\033[1;32mExpense deleted successfully!\033[m")

                        question = int(input(ui.REPEAT_DELETE_MENU))

                        if question == 1:
                            continue

                        else:
                            break

                    else:
                        continue
                    
                else:
                    print("\nInvalid number.")
                    continue

    elif start == 4:
        break

    else:
        print("\nInvalid action.")