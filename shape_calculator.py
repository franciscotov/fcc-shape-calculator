import math

class Rectangle:
    width = 1
    height = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height
        #print('Constructed...')

    def __str__(self) -> str:
        #if self.width == self.height:
        #    return 'Square(side=' + str(self.width) + ')'
        #else:
        return 'Rectangle(width='+ str(self.width)+ ', height=' + str(self.height) +')'

    def get_picture(self):
        s = ''
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                s = s + '*'
            s = s +'\n'
        return s

    def set_width(self, width):
        self.width = width
        #print('set width')

    def set_height(self, height):
        self.height = height
        #print('set height')
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) **.5

    def get_amount_inside(self, figure):
        W = self.width / figure.width
        H = self.height / figure.height
        return math.floor(W * H)

class Square(Rectangle):
    side = 0
    def __init__(self, side):
        self.set_width(side)
        self.set_height(side)
        self.side = side
        #print('Square', self.width, self.height, self.side)
    
    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side
    
    def __str__(self) -> str:
        return 'Square(side=' + str(self.width) + ')'