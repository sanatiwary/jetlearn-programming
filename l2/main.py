class Car:
    def __init__(self, brand, model, fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    def showCar(self):
        print("my car is a {} {}, model {}, using {} fuel".format(self.color, self.brand, self.model, self.fuel))

class Convertible(Car):
    def __init__(self, brand, model, fuel, color, transmission, turbo):
        Car.__init__(self, brand, model, fuel, color)
        self.transmission = transmission
        self.turbo = turbo

buick50 = Convertible("buick", "1949 50 super convertible", "petrol", "blue", "automatic", False)

print(buick50.getColor())
buick50.setColor("light blue")

print(buick50.showCar())