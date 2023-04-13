from main import Fruit, Car, Student, Teacher, Principal

# Start creating fruits out of the fruit class
first_fruit = Fruit("Yellow", "Oval", "200g", "Sweet")
second_fruit = Fruit("Orange", "Spherical", "150g", "Sour")

print(first_fruit.color)

first_car = Car("BMW", "KDH 450 P", "dark blue", "Ksh 15M")
second_car = Car("Benz", "KDJ 795 L", "black", "Ksh 10M")

second_car.accelerate()
print(first_car.price)

principal_one = Principal("Mrs.Esther", "esther@gmail.com", "123")

principal_one.register()


