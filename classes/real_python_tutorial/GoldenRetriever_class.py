class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound = 'arf-arf'): # add default sound of barking for parent Dog() class
        return f"{self.name} barks: {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "woof-woof"): # add sound of barking for child class
        return super().speak(sound) # super() func find class where inherit required information


jack = GoldenRetriever('Jack', 3)
tim = Dog('Tim', 5)

print(jack.speak())
print(tim.speak())

