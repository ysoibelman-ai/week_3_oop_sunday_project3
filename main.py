
from classes.employee_class import Employee
from classes.intern_class import Intern
from classes.manager_class import Manager
def main():
    staff = [
    Employee("Dana", 12000),
    Manager("Avi", 20000, 3000),
    Intern("Noa", 6000, 6),]
 
    for person in staff:
        print(person.describe())
    
    try:
        Intern("Tom", 5000, 0)
    except ValueError as error:
        print("error:", error)
    
    total = 0
    for person in staff:
        total = total + person.monthly_cost()
    print("Total monthly cost:", total)

if __name__ == "__main__":
    main()