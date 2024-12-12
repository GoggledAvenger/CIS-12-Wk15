from animal import Animal
from dog import Dog

# Demonstration
generic_animal = Animal("Generic Animal")
dog = Dog("Buddy",'curly')

print(generic_animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())             # Output: Buddy barks.