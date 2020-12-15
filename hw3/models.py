from day import day_count


class UnableToWorkException(Exception):
	def __str__(self):
		return "I’m not hired yet, lol."

class Employee:
	def __init__(self,name,email,salary):
		self.name = name 
		self.email = email 
		self.salary = salary 
		self.check_email()
		self.save_email()

	def work(self):
		return "I come to the office."

	def check_salary(self):
		return self.salary * day_count

	def __ge__(self,other):
		return self.salary >= other.salary

	def save_email(self):
		with open("email.txt", "a+") as file:
			file.write(self.email + " ")

	def check_email(self):
		with open("email.txt", "r") as file:
			file.seek(0)
			if self.email in file.read():
				raise ValueError


class Recruiter(Employee):
	def __init__(self,name,email,salary,hired_this_month=0):
		super().__init__(name,email,salary)
		self.hired_this_month = hired_this_month

	def work(self):
		text = super().work()[0:-1] 
		return text + " and start to hiring."

	def __str__(self):
		return f"{self.name}:{self.email}"


class Programmer(Employee): 
	def __init__(self,name,email,salary,tech_stack=0,closed_this_month=0):
		super().__init__(name,email,salary)
		self.tech_stack = tech_stack
		self.closed_this_month = closed_this_month

	def work(self):
		text = super().work()[0:-1] 
		return text + " and start to coding."
	
	def __str__(self):
		return f"{self.name} {self.email} {self.salary} {self.tech_stack}"

	def __le__(self,other):
		return self.tech_stack <= other.tech_stack

	def __add__(self,other):
		return Programmer("Ivan","i956@gmail.com",400,(self.tech_stack + other.tech_stack))


class Candidate():
	def __init__(self,full_name,email,technologies,main_skill,main_skill_grade):
		self.full_name = full_name
		self.email = email
		self.technologies = technologies
		self.main_skill = main_skill
		self.main_skill_grade = main_skill_grade

	def work(self):
		raise UnableToWorkException


class Vacancy():
	def __init__(self,title,main_skill,main_skill_level):
		self.title = title 
		self.main_skill = main_skill 
		self.main_skill_level = main_skill_level