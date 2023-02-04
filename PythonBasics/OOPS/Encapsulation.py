class Employee:

    def __init__(self, name, salary, project):
        self._name = name
        self.__salary = salary
        self.project = project

    def show_emp_details(self):
        print("Name is : ", self._name, " and Salary is - ", self.__salary)


    def show_emp_workdata(self):
        print("Emp name is : ", self.name, " and Current project is - ", self.project)


class FinanceDepartMent(Employee):

    def show_super_details(self):
        super().show_emp_details()


# f_dept = FinanceDepartMent("Jessica", 40000, "Marven")
# f_dept.show_super_details()
emp = Employee("Jessica", 40000, "Marven")
emp.show_emp_details()
print(emp._name)
# emp.show_emp_workdata()