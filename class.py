class Cookie:
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color=color

Cookie_one = Cookie('green')

Cookie_two = Cookie('bule')

print('Cookie one color is: ',Cookie_one.get_color())
print('Cookie two color is: ',Cookie_two.get_color())
