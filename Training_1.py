'''

x = "hELLO My FriEnDs!!! thIS A tE%sT For your #p#r#o#b#l#e#m a"


y = filter(lambda x: not x.isalpha(), x)
print(list(y))

'''
'''
from tabulate      import tabulate

x = ['course']
y = [
    ["p"], ['g'], ['f'], ['c++']
    ]

print(tabulate(y, headers = x, tablefmt = "grid"))

education_courses = {"Course": ["Python", "Kotlin", "C++", "Java", "PHP"]}

for i in education_courses.values():
    for x in i:
        print(x)

p = [x for x in education_courses]
o = [[y] for x in education_courses.values() for y in x]

print(p)
print(o)
'''
'''
class Signin:
    number_of_users = 0
    
    def __init__(self, first_name, last_name):
        self.name = first_name 
        self.family = last_name
        Signin.number_of_users += 1
        
    
    def user_info(self):
        print(f"name: {self.name}\nlast name: {self.family}")


class Course:
    
    def __init__(self, course_info):
        self.courses = course_info 
        
        if self.number_of_users > 0:
            print("user is available")  
        
    
    def course_information(self):
        pass
    
    
    def buy_course(self):
        pass
   
  
class User(Signin, Course):
    
    def servise(self):
        x = input("Enter x or y: ")
        
        if x == 'x':
            Signin.__init__(self, "amir", "Elyasi")
        
        else:
            Course.__init__(self,67989)
               
    def purchase_information(self):
        pass
    
    
person = User("amir", "Elyasi")    
print(person.number_of_users)
person.servise()
print(person.number_of_users)
'''

'''
x = [0,0,0,0,0,1,1,1,1,1]

if x.count(0) + x.count(1) != 9:
    print("Yesssssssssssssss")
    

print(x.count(0) + x.count(1))
print(list(range(1, 10)))
'''
from colorama import Fore
from random import choices
x = 112322
y = 32233


 
id_number_list = []

# Create clothe id 
while len(id_number_list) != 10:
    number_str = ""
    choice_number = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=5)
    if choice_number[0] == 0:
        continue
    
    for number in choice_number:
        number_str += str(number)
    
    if number_str in id_number_list:
        continue
    else:
        id_number_list.append(number_str)
        
print(id_number_list)
print(id_number_list[0])

a = 1000

print(str(a + 1))








































