class CoffeMachine:
	water = 25 
	grains = 25 
	_curent_trash = 0
	__max_trash = 40

	def make_cappuccino(self):
		if self.out_of_water():
			print("Закончилась вода")
			self.add()
		elif self.out_of_grains():
			print("Закончились зерна")
			self.add()
		elif self.isfull(10):
			print("Кофеварку нужно почистить")
			self.add()
		else:
			self.water -= 7
			self.grains -= 7
			self._curent_trash += 10
			print("Капучино готово")

	def make_espresso(self):
		if self.out_of_water():
			print("Закончилась вода")
			self.add()
		elif self.out_of_grains():
			print("Закончились зерна")
			self.add()
		elif self.isfull(10):
			print("Кофеварку нужно почистить")
			self.add()
		else: 
			self.water -= 14
			self.grains -= 12 
			self._curent_trash += 10
			print("Эспрессо готово")

		

	def out_of_water(self):
		return self.water <= 0 

	def out_of_grains(self):
		return self.grains <= 0

	def isfull(self,trash):
		return self._curent_trash + trash > self.__max_trash

	def add(self):
		if self.out_of_water():
			self.water = 25 
		elif self.out_of_grains():
			self.grains = 25 
		else:
			self._curent_trash = 0


class CoffeMilkMachine(CoffeMachine):
	milk = 60 

	def make_latte(self):
		if self.out_of_water():							
			print("Закончилась вода")
			self.add()
		elif self.out_of_grains():
			print("Закончились зерна")	
			self.add()
		elif self.isfull(10):
			print("Кофеварку нужно почистить")
			self.add()
		else:
			self.water -= 5
			self.grains -= 6
			self._curent_trash += 10
			print("Латте готово")

	def make_cappuccino(self):
		if self.out_of_water():
			print("Закончилась вода")
			self.add()
		elif self.out_of_grains():
			print("Закончились зерна")
			self.add()
		elif self.isfull(15):
			print("Кофеварку нужно почистить")
			self.add()
		else:
			self.water -= 8
			self.grains -= 16
			self._curent_trash += 15
			print("Капучино готово")


	def add_milk(self):
		if self.out_of_milk():
			print("Молоко кончилось")
			self.refill_milk()
		else:
			self.milk -= 15
			print("Молоко добавлено")

	def out_of_milk(self):
		return self.milk < 0

	def refill_milk(self):
		self.milk = 60

class CoffeСognacMachine(CoffeMilkMachine):
	cognac = 12 

	def add_cognac(self):
		if self.out_of_cognac():
			print("Коньяк закончилась")
			self.refill_cognac()
		else:
			self.cognac -= 4
			print("Коньяк добавлен")

	def out_of_cognac(self):
		return self.cognac < 0

	def refill_cognac(self):
		self.cognac = 12

# my = CoffeСognacMachine()
# [my.make_cappuccino() for i in range(5)]
# [my.add_milk() for i in range(5)]
# [my.add_cognac() for i in range(5)]