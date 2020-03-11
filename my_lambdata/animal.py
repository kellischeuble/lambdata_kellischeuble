class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.sound} " * 3


animal_1 = Animal("Cat", "Meow")

print(animal_1.speak())
