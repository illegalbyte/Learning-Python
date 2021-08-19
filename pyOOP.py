#! python3

# this starts a creates an object 'Dog'
class Dog:
	# this initialises the dog class, and states it takes 3 inputs (itself, name, and age)
	def __init__(self, name, age):
		self.name = str(name)
		self.age = int(age)

	def change_name(self, name):
		self.name = name


dog1 = Dog("Sasha", 16)
print(f'{dog1.name} {dog1.age}')

dog1.change_name('Becky')
print(f'{dog1.name} {dog1.age}')


################################
# Student example: 
################################

class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade # 0 - 100

	def get_grade(self):
		return self.grade

class Course: 
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = [] # note that this isn't one of the attributes being passed at __init__

	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		else:
			return False

	def get_average_grade(self):
		sumOfGrades = 0;
		for student in self.students:
			sumOfGrades += student.get_grade()
		return sumOfGrades / len(self.students)

		pass


s1 = Student("Lewis", 22, 81)
s2 = Student("Neha", 19, 78)
s3 = Student("Alisha", 19, 79)
	
course = Course('Contract Law', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())


#################################
# Inheritance:					#
#################################

################################
# 		Without inheritance: 
class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def speak(self):
		print("meow")


class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def speak(self):
		print("woof") # the only difference is that the dog woofs instead of meows,
		# how can we rewrite this so it uses less code?
################################


################################
# 		With Inheritance: 
class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet): # by passing Pet class, Cat inherits all the methods and attributes of Pet
	def speak(self):
		print("Meow")


class Dog(Pet):  # by passing Pet class, Dog also inherits all the methods and attributes of Pet
	def speak(self):
		print("Woof")

class Fish(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age) # We initialise inheriting the name and age values at lines 98 and 99
		self.color = color # we add the color attribute to Fish, 

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old, and I'm a {self.color} colour")


cat1 = Cat('Nina', 2)
cat1.show()

fish = Fish("Nemo", 1, "orange")
fish.show()
################################
