class Vector2D():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = self.x2 - self.x1
        self.y = self.y2 - self.y1

        self.name = "vN"
        self.color = "#cecece"
    
    def __str__(self):
        return "(%i, %i)" % (self.x, self.y)
    
    def getPos(self):
        return self.x1, self.y1, self.x2, self.y2

    # Soma
    def __add__(self, v2):
        return Vector2D(self.x1, self.y1, v2.x2, v2.y2)
