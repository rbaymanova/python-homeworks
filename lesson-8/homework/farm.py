class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cow")

    def make_sound(self):
        print(f"{self.name} says Moo!")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken")

    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def lay_egg(self):
        print(f"{self.name} laid an egg!")


class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Sheep")

    def make_sound(self):
        print(f"{self.name} says Baa!")

    def grow_wool(self):
        print(f"{self.name} is growing wool.")


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the farm.")

    def list_animals(self):
        print("Animals on the farm:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.species}), {animal.age} years old")


# Example Usage
farm = Farm()
cow = Cow("Bessie", 5)
chicken = Chicken("Clucky", 2)
sheep = Sheep("Dolly", 3)

farm.add_animal(cow)
farm.add_animal(chicken)
farm.add_animal(sheep)

farm.list_animals()

cow.eat()
cow.make_sound()
cow.produce_milk()

chicken.sleep()
chicken.make_sound()
chicken.lay_egg()

sheep.eat()
sheep.make_sound()
sheep.grow_wool()
