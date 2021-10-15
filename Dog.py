
class Dog():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting. ")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog("Arya", 6)
print("My dogs name is " + my_dog.name.title()+".")
print("My dogs age is " + str(my_dog.age)+".")
my_dog.sit()
my_dog.roll_over()