class T:
    def __init__(self, color:str, size:str) :
    
        self.color = color
        self.size = size
        self.wetness: int = 0

toalha = T("green", "g")
print(toalha.color)
print(toalha.size)