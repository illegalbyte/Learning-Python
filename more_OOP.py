class employee: 
	raise_amount = 1.04
	number_of_employees = 0

	def __init__(self, first, last, pay: float) -> None:
		self.first = first
		self.pay = pay
		self.email = f"{first}.{last}@company.com"
		employee.number_of_employees += 1

	def full_name(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

Lewis = employee("Lewis", "Gentle", 30000)


print(Lewis.pay)
Lewis.apply_raise()
print(Lewis.pay)

# print namespace __dict__
print(Lewis.__dict__)
print(employee.__dict__)
