class Dog:
    # class attributes
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    # Another instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'

    

lord = Dog('Lord', 5)
jack = Dog('Jack', 11)

print(jack)
print()

print(lord.speak('Wow'))



