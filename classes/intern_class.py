from classes.employee_class import Employee
class Intern (Employee):
    def __init__(self, name, salary,intern_months):
        if  not (1 <= intern_months <=12):
            raise ValueError (" months must be  1-12")
        super().__init__(name, salary)
        self.intern_months = intern_months

    def title(self):
        return "Intern"