class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real, "i + ",self.img,"j" )

    # def add(self, num2):               #this will give an error
        # newReal = self.real + num2.real
        # newImg = self.img + num2.img
        # return Complex(newReal, newImg)

    def __add__(self, num2):        #this is a dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):        #this is a dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 - num2      # the + operator utilises the dunder function here which adds the complex number through our defined logic
num3.showNumber()

        
# plus or minus ka mtlb hi change krdiya yaha (operation overloading)  Yahi mtlb hai polymorphism ka