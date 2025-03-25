import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"

class EmployeeManager:
    def __init__(self, file_name="employees.txt"):
        self.file_name = file_name

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        
        with open(self.file_name, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Employee added successfully!\n")

    def view_employees(self):
        if not os.path.exists(self.file_name):
            print("No employee records found.\n")
            return
        
        with open(self.file_name, "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.\n")
                return
            
            for record in records:
                employee_id, name, position, salary = record.strip().split(",")
                print(f"ID: {employee_id}, Name: {name}, Position: {position}, Salary: {salary}")
            print()

    def search_employee(self):
        search_id = input("Enter Employee ID to search: ")
        found = False

        with open(self.file_name, "r") as file:
            for record in file:
                employee_id, name, position, salary = record.strip().split(",")
                if employee_id == search_id:
                    print(f"ID: {employee_id}, Name: {name}, Position: {position}, Salary: {salary}\n")
                    found = True
                    break
        
        if not found:
            print("Employee not found.\n")

    def update_employee(self):
        search_id = input("Enter Employee ID to update: ")
        updated_records = []
        found = False

        with open(self.file_name, "r") as file:
            records = file.readlines()

        for record in records:
            employee_id, name, position, salary = record.strip().split(",")
            if employee_id == search_id:
                print("Employee found! Enter new details:")
                name = input("Enter new name: ") or name
                position = input("Enter new position: ") or position
                salary = input("Enter new salary: ") or salary
                found = True
            updated_records.append(f"{employee_id},{name},{position},{salary}\n")
        
        if found:
            with open(self.file_name, "w") as file:
                file.writelines(updated_records)
            print("Employee updated successfully!\n")
        else:
            print("Employee not found.\n")

    def delete_employee(self):
        search_id = input("Enter Employee ID to delete: ")
        updated_records = []
        found = False

        with open(self.file_name, "r") as file:
            records = file.readlines()

        for record in records:
            employee_id, name, position, salary = record.strip().split(",")
            if employee_id == search_id:
                found = True
                continue
            updated_records.append(record)
        
        if found:
            with open(self.file_name, "w") as file:
                file.writelines(updated_records)
            print("Employee deleted successfully!\n")
        else:
            print("Employee not found.\n")

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()