# employee_salary.py

employees = {}


def add_employee():
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employees[name] = salary
    print("Employee added successfully.")


def display_employees():
    if not employees:
        print("No employee records found.")
        return

    print("\nEmployee Salary Details")
    print("-----------------------")
    for name, salary in employees.items():
        print(f"{name} : ₹{salary:.2f}")


def highest_salary():
    if not employees:
        print("No records available.")
        return

    highest = max(employees.values())

    print("\nEmployee(s) with Highest Salary:")
    for name, salary in employees.items():
        if salary == highest:
            print(f"{name} : ₹{salary:.2f}")


def average_salary():
    if not employees:
        print("No records available.")
        return

    avg = sum(employees.values()) / len(employees)
    print(f"\nAverage Salary: ₹{avg:.2f}")


while True:
    print("\nEmployee Salary Management")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Highest Salary")
    print("4. Average Salary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        highest_salary()

    elif choice == "4":
        average_salary()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid choice.")