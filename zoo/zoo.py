class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    # def add_lion(self, name,age):
    #     self.animals.append(Lion(name,age) )
    # def add_tiger(self, name,age):
    #     self.animals.append( Tiger(name,age) )
    # def add_bear(self,name,age):
    #     self.animals.append(Bear(name,age))
    
    def add_animal(self, animal):
        self.animals.append(animal)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
class Animal:
    def __init__(self,name,age,health_level,happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
    
    def display_info(self):
        print(f" name {self.name} age : {self.age} health : {self.health_level} happiness: {self.happiness_level}")

    def feed(self):
        self.happiness_level +=10
        self.health_level += 10

class Lion(Animal):
    def __init__(self, name, age,health_level= 70, happiness_level=80):
        super().__init__(name, age, health_level, happiness_level)
        self.roar = "roar" #new attribute 
    def feed(self):
        self.happiness_level +=10
        self.health_level += 10

class Tiger(Animal):
    def __init__(self, name, age, health_level =70, happiness_level = 60):
        super().__init__(name, age, health_level, happiness_level)
        self.color = "stripe"
    def feed(self):
        self.happiness_level +=10
        self.health_level += 10

class Bear(Animal):
    def __init__(self, name, age, health_level = 70, happiness_level=80):
        super().__init__(name, age, health_level, happiness_level)
        self.swim = "a swimmer" 
    def feed(self):
        self.happiness_level +=10
        self.health_level += 10




    


zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala", 3))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Tiger("Rajah", 5))
zoo1.add_animal(Tiger("Shere Khan", 7))
zoo1.add_animal(Bear("Baloo", 6))
zoo1.add_animal(Bear("Paddington", 2))

zoo1.print_all_info()

for animal in zoo1.animals:
    animal.feed()
zoo1.print_all_info()


