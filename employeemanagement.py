from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, basicSalary):
        self.name = name
        self.basicSalary = basicSalary

    @abstractmethod
    def calculateSalary(self):
        pass

    def displayDetails(self):
        print("Name:", self.name)
        print("Basic Salary:", self.basicSalary)


class Developer(Employee):

    def calculateSalary(self):
        bonus = 5000
        return self.basicSalary + bonus


class Manager(Employee):

    def calculateSalary(self):
        bonus = 10000
        return self.basicSalary + bonus


class Tester(Employee):

    def calculateSalary(self):
        bonus = 3000
        return self.basicSalary + bonus


def startprogram():

    developer = Developer("karan", 30000)
    manager = Manager("riya", 40000)
    tester = Tester("ankitha", 25000)

    employees = [developer, manager, tester]

    for employee in employees:

        employee.displayDetails()

        salary = employee.calculateSalary()

        print("Final Salary:", salary)
        print()


startprogram()