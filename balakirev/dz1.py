from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


person = Person("Fedor", 38)

tm = Template("My name is {{ p.getName() }} and I'm {{ p.getAge() }} years old ")
msg = tm.render(p=person)

if __name__ == "__main__":
    print(msg)
