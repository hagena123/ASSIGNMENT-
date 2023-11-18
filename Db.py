def information_of_employee():
    employee = {}
    employee["Employee ID"] = input("Enter ID of Employee: ")
    employee["First Name"] = input("Enter First Name of Employee: ")
    employee["Last Name"] = input("Enter Last Name of Employee: ")
    employee["Date of Birth"] = input("Enter Date of Birth of Employee (YYYY-MM-DD): ")
    employee["Sex"] = input("Enter Sex of Employee (M/F): ")
    employee["Year of Recruitment of Employee"] = int(input("Enter Year of Recruitment: "))
    employee["Salary"] = float(input("Enter Salary of Employee: "))
    return employee

def main():

    num_employees = int(input("Enter the number of employees: "))

 
    employee_db = []

  
    for _ in range(num_employees):
        print(f"\nEnter information for Employee {_ + 1}:")
        employee = information_of_employee()
        employee_db.append(employee)


    print("\nEmployee Database:")
    for employee in employee_db:
        print("\nEmployee ID:", employee["Employee ID"])
        print("First Name:", employee["First Name"])
        print("Last Name:", employee["Last Name"])
        print("Date of Birth:", employee["Date of Birth"])
        print("Sex:", employee["Sex"])
        print("Year of Recruitment:", employee["Year of Recruitment"])
        print("Salary:", employee["Salary"])

if __name__ == "__main__":
    main()
