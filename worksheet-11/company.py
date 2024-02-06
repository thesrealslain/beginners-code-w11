"""
A growing business is finding it increasingly difficult to manage all the workers they have. 
So, the CEO asks you to develop a system to keep track of everyone. 
Write your solutions based on the requirements below and save it as company.py.
Each worker they have has their own unique identifier, 
name, and job title. These are just some details you may choose to store for each worker.
The company has two kinds of workers: employees and contractors. 
The employees are on a fixed monthly salary. But there's a catch: they can be promoted, 
and when that happens, their salary goes up (starting with £500, £1000 and then £2000 increase).
As for the contractors, they're paid by the hour. Sometimes they work extra hours, 
and the CEO needs the system to account for that because it affects how much they're paid.
Finally, the business is growing, so they are always adding new people. Sometimes employees,
sometimes contractors. On the flip side, the business does have to let people go from time to time. 
So, the system should be able to remove someone based on their unique identifier.
One more thing: For budgetary reasons, 
the CEO needs to know how much they are spending on salaries for everyone—both employees and contractors, 
and the system should be able to tell me how many employees and contractors there are.
"""

class Worker:
    def __init__(self, identifier, name, job_title):
        self.identifier = identifier
        self.name = name
        self.job_title = job_title

    def __str__(self):
        return f"{self.job_title} {self.name} (ID: {self.identifier})"


class Employee(Worker):
    def __init__(self, identifier, name, job_title, salary):
        super().__init__(identifier, name, job_title)
        self.salary = salary

    def promote(self):
        self.salary += 500

    def get_salary(self):
        return self.salary


class Contractor(Worker):
    def __init__(self, identifier, name, job_title, hourly_rate, hours_worked=0):
        super().__init__(identifier, name, job_title)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def add_hours_worked(self, hours):
        self.hours_worked += hours

    def get_salary(self):
        return self.hourly_rate * self.hours_worked


class Company:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def remove_worker(self, identifier):
        self.workers = [worker for worker in self.workers if worker.identifier != identifier]

    def get_total_salary_budget(self):
        total_salary_budget = sum(worker.get_salary() for worker in self.workers)
        return total_salary_budget

    def get_num_employees(self):
        return sum(isinstance(worker, Employee) for worker in self.workers)

    def get_num_contractors(self):
        return sum(isinstance(worker, Contractor) for worker in self.workers)


# Test the company system
def test_company_system():
    company = Company()

    employee1 = Employee("E001", "John Doe", "Software Engineer", 60000)
    contractor1 = Contractor("C001", "Jane Doe", "Freelancer", 25, 40)

    company.add_worker(employee1)
    company.add_worker(contractor1)

    print("Initial Workers:")
    for worker in company.workers:
        print(worker)

    print("\nTotal Salary Budget:", company.get_total_salary_budget())
    print("Number of Employees:", company.get_num_employees())
    print("Number of Contractors:", company.get_num_contractors())

    employee1.promote()
    contractor1.add_hours_worked(10)

    print("\nAfter Promotion and Extra Hours:")
    for worker in company.workers:
        print(worker)

    print("\nUpdated Total Salary Budget:", company.get_total_salary_budget())


if __name__ == "__main__":
    test_company_system()
