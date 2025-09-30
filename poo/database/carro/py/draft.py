class Car:
    def __init__(self, pas:int ,km:int ,gas:int, pasMax:int, gasMax:int):
        self.pas: int = pas
        self.km: int = km
        self.gas: int = gas
        self.pasMax: int = pasMax
        self.gasMax: int = gasMax


    def __str__(self) :
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"

    def enter(self) ->None:
        if self.pas < self.pasMax:
            self.pas += 1     
        else:
            print( f"fail: limite de pessoas atingido")
       
    def leave(self) ->None:
        if self.pas > 0:
            self.pas -= 1
        else:
            print( f"fail: nao ha ninguem no carro")

    def fuel(self,amount:int) :
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax
    
    def drive(self,amount:int) ->None:
        if self.pas==0:
            print( f"fail: nao ha ninguem no carro")
            return
        if self.gas==0:
            print( f"fail: tanque vazio")
            return
        if amount > self.gas:
            self.km += self.gas
            print( f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
            return
        self.km += amount
        self.gas -= amount





def main():
    carro= Car(0,0,0,2,100)
    while True:
        line  = input()
        args = line.split (" ")
        print("$" + line)

        if args[0] == "end":
            break

        if args[0] == "show":
            print(carro)

        if args[0] == "enter":
            carro.enter()

        if args[0] == "leave":
            carro.leave()

        if args[0] == "fuel":
            carro.fuel(amount=int(args[1]))
        
        if args[0] == "drive":
            carro.drive(amount=int(args[1]))

main()
