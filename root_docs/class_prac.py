class Dog:
    def __init__(self, name, age, color, sex):
        self.name = name
        self.age = age
        self.color = color
        self.sex = sex 
    def __str__(self):
        return self.name, self.age, self.color , self.sex  
    
d1= Dog('driver', 1, 'black', 'male')

print(d1.age)

