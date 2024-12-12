from animal import Animal

# Child class
class Dog(Animal):

    def __init__(self, name, tail=None):
        super().__init__(name)
        self.tail = tail

    def speak(self):
        return f"{self.name} barks and has a {self.tail} tail."