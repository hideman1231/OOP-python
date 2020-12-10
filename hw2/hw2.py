from day import day_count

class Employee:
	def __init__(self,name,email,salary):
		self.name = name 
		self.email = email 
		self.salary = salary 

	def work(self):Recruiter
		return "I come to the office."

	def check_salary(self):
		return self.salary * day_count

	def __ge__(self,other):
		return self.salary >= other.salary

class Recruiter(Employee):
	def __init__(self,name,email,salary,hired_this_month = 0):
		super().__init__(name,email,salary)
		self.hired_this_month = hired_this_month

	def work(self):
		text = super().work()[0:-1] 
		return text + " and start to hiring."

	def __str__(self):
		return f"{self.name}:{self.email}"

class Programmer(Employee): 
	def __init__(self,name,email,salary,tech_stack = 0,closed_this_month = 0):
		super().__init__(name,email,salary)
		self.tech_stack = tech_stack
		self.closed_this_month = closed_this_month

	def work(self):
		text = super().work()[0:-1] 
		return text + " and start to coding."
	
	def __str__(self):
		return f"{self.name}:{self.email}"

	def __le__(self,other):
		return self.tech_stack <= other.tech_stack

	def __add__(self,other):
		return self.tech_stack + other.tech_stack

# a1 = Programmer('Dima','smakvlad@gmail.com', 300, 2, 2)
# a2 = Programmer('Misha','oraora@gmail.com.com', 200, 4)
# b1 = Recruiter('Oleg','kakaka@gmail.com',100)
# print(a1.__str__())
# print(a1.work())
# print(a1.__le__(a2))
# print(a1.__add__(a2))
# print(b1.check_salary())

