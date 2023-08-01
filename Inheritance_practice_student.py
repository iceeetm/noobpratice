#繼承的練習
from Inheritance_practice_person import person
            
class student(person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        
    def print_name(self):
        print(self.name)
        
    def print_age(self):
        print(self.age)
    
    def print_school(self):
        print(self.school) 
    
    
student1 = student('小明', 52, '小明國小')

student1.print_name()
student1.print_age()
student1.print_school()
    