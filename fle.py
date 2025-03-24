class Veicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("driving")

class Plane(Vehicle):
    def move(self):
        print("flying")

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

clas Dog(Animal):
    def move(self):
        print("running")

class Bird(Animal):
    def move(self):
        print("Flapping wings")

if __name__ == "__main__":
    vehicles=[Car(), Plane()]
    animals=[Dog(), Bird()]

    for vehicle in vehicles:
        vehicle.move()
    for animal in animals:
        animal.move()


