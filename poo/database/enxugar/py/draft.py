class T:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness(self):
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        return 0 # se não for P, M ou G
            
    def dry(self, amount:int):
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()
            

    def wringOut(self):
        self.wetness = 0

    def isDry(self) -> bool :
            return self.wetness == 0

    def __str__(self):
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"
    

def main():
    toalha = T("", "")
    while True:
        line = input()
        args = line.split(" ")
        print('$' + line)

        if args[0] == "end":
            break

        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            toalha = T(color, size)

        elif args[0] == "mostrar":
            print(toalha)

        elif args[0] == "enxugar": 
            amount = int(args[1])
            toalha.dry(amount)
            if toalha.wetness > toalha.getMaxWetness():   
                print("toalha encharcada")
                toalha.wetness = toalha.getMaxWetness()

        elif args[0] == "seca":
            if toalha.isDry()  :
                print("sim")
            else:
                print("nao")  

        elif args[0] == "torcer":
            toalha.wringOut()

        

        else:
            print("Comando inválido")

main()