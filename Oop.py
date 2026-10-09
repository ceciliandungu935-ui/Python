class Student:
    def __init__(self, name, age , gender , hobby):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print("Student is studying")
    def sing(self):
        print("Student is singing")

student1 = Student("Eric", 45, "male" ,"dancing")
print(student1.name)
student1.study()

student2 = Student("Talia" , 60, "female" ,"sidequest")
print(student2.gender)
student2.sing()

student3 = Student("Daniel" , 90, "male" ,"cooking")