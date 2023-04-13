class Fruit:
    # This is a constructor
    def __init__(self, color, shape, size, taste):
        self.color = color
        self.shape = shape
        self.size = size
        self.taste = taste

class Car:
    def __init__(self, model, reg_no, color, price):
        self.model = model
        self.reg_no = reg_no
        self.color = color
        self.price = price

    def brake(self):
        print("Yeah, I can brake")

    def accelerate(self):
        print("Yeah, I can accelerate")


class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print("You registered with email", self.email,
              "and password", self.password)

    def login(self):
        # let's assume the user had already registered
        if self.email == "example@gmail.com" and self.password == "123":
            print("You logged in successfully")
        else:
            print("Wrong username or password")


class Teacher(Student):
    def suspend_student(self):
        print("Yeah, I can suspend a student")

    def submit_results(self):
        print("Yeah, I can submit results")


class Principal(Teacher):
    def suspend_teacher(self):
        print("Yeah, I can suspend a teacher")

    def schedule_meeting(self):
        print("Yeah, I can schedule a meeting")
