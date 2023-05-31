class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.__breed = breed

def main():
    fido = Dog("Fido", 3, "Labrador")
    print(fido.name)
    print(fido.age)
    print(fido.__breed)