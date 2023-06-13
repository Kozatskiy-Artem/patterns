"""Implementation of the Visitor pattern"""

from abc import ABC, abstractmethod


class Visitor(ABC):
    """
    The Visitor Interface declares a set of visiting methods that correspond to
    component classes. The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing with.
    """
    @abstractmethod
    def visit_company(self, company) -> None:
        pass

    @abstractmethod
    def visit_department(self, department) -> None:
        pass

    @abstractmethod
    def visit_employee(self, employee) -> None:
        pass


class ReportGenerator(Visitor):
    def visit_company(self, company) -> None:
        print(f"Зарплатна відомість для компанії {company.name}")
        for department in company.departments:
            department.accept(self)
        print("\n")

    def visit_department(self, department) -> None:
        print(f"Департамент: {department.name}")
        for employee in department.employees:
            employee.accept(self)

    def visit_employee(self, employee) -> None:
        print(f"- {employee.position}: {employee.salary}")


class Component(ABC):
    """
    The Component interface declares an `accept` method that should take the
    base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Company(Component):
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_company(self)


class Department(Component):
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_department(self)


class Employee(Component):
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_employee(self)


if __name__ == '__main__':
    employee1 = Employee("Менеджер", 5000)
    employee2 = Employee("Розробник", 7000)
    employee3 = Employee("Аналітик", 6000)

    department1 = Department("Відділ продажу", [employee1, employee2])
    department2 = Department("Відділ розробки", [employee1, employee3])

    company1 = Company("DigitalMindsUA", [department1, department2])

    report_generator = ReportGenerator()

    company1.accept(report_generator)

    department1.accept(report_generator)
