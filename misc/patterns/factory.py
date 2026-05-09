from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Duck(Animal):
    def make_sound(self):
        return "Quack!"


class AnimalFactory:
    @staticmethod
    def make_animal(animal: str) -> Animal:
        match (animal.lower().strip()):
            case "dog":
                return Dog()
            case "cat":
                return Cat()
            case "duck":
                return Duck()
            case _:
                raise ValueError("Invalid animal type. Choose 'dog', 'cat', or 'duck'")

if __name__ == "__main__":
    instance = AnimalFactory.make_animal("cat")
    print(instance.make_sound())
