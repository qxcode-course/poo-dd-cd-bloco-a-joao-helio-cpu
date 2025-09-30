class Calc:
    def __init__(self,display:float, battery:int, batMax:int):
        self.display= display
        self.battery= battery
        self.batMax:int = batMax       

    def __str__(self) :
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def battMax(self,amount:int) ->None:
        self.batMax += amount
        if self.battery > self.batMax:
            self.battery = self.batMax
            return
    
    
    def charge(self,amount:int):
        self.battery += amount
        if self.battery > self.batMax:
            self.battery = self.batMax
        
    
    def sum(self,a:float,b:float) ->None:
        if self.battery == 0:
            print( f"fail: bateria insuficiente")
            return
        self.battery -= 1
        self.display = a + b
        
    def div(self,num:float,den:float) ->None:
        if self.battery == 0:
            print( f"fail: bateria insuficiente")
            return
        self.battery -= 1

        if den == 0:
            print( f"fail: divisao por zero")
            return
        
        
        self.display = num / den
        
        

def main():
    calculadora= Calc(0,0,0)
    while True:
        line  = input()
        args = line.split (" ")
        print("$" + line)

        if args[0] == "end":
            break

        if args[0] == "show":
            print(calculadora)

        if args[0] == "init":
            calculadora= Calc(0,0,int(args[1]))

        if args[0] == "charge":
            calculadora.charge(int(args[1]))

        if args[0] == "sum":
            calculadora.sum(float(args[1]),float(args[2]))

        if args[0] == "div":
            calculadora.div(float(args[1]),float(args[2]))

        
            

main()