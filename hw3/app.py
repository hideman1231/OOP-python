import traceback

from models import *


def main(): 
	prog1 = Programmer('Dima','smakvlad@gmail.com', 300, 2, 2)
	prog2 = Programmer('Misha','oraora@gmail.com.com', 200, 4)
	recr1 = Recruiter('Oleg','kakaka@gmail.com',100)
	cand1 = Candidate('Vasya Pupkin','vasya@gmail.com',0,'backend',1)
	cand2 = Candidate('Igor Kreed','igorK@gmail.com',2,'midle',2)
	cand3 = Candidate('Sasha Lapin','lapasa@gmail.com',3,'Django',3)
	vac1 = Vacancy("help",'Django',2)
	vac2 = Vacancy("frontend","JS",3)
	# print(prog1.__str__())
	# print(prog1.work())
	# print(prog1.__le__(prog2))
	# print(recr1.check_salary())
	# print(recr1.work())
	# print(prog1.__add__(prog2))
	print(cand2.work())  # Вызывает ошибку UnableToWorkException

if __name__ == '__main__':
	try: 
		main()
	except Exception as err:
		err = traceback.format_exc()
		with open("logs.txt","w") as file:
			file.write(err)
		