class A:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self) :
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, amount:int):
        self.age += amount
        if self.age >= 4:
            print( f"warning: {self.species} morreu")
        return ""

    def makeSound(self) ->None:
        if self.age ==0 :
            print("---")
        elif self.age >= 4:
            print("RIP")
        else:
            print(self.sound)

    def growMax(self):
        if self.age >= 4:
            self.age = 4

        

        
        
    
def main():
    animal= A("","")
    while True:
        line  = input()
        args = line.split (" ")
        print("$" + line)

        if args[0] == "end":
            break

        if args[0] == "show":
            print(animal)

        if args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = A(species, sound)

        if args[0] == "grow":
            amount = int(args[1])
            animal.ageBy(amount)
            animal.growMax()

        if args[0] == "noise":
            animal.makeSound()
        
        

main()
