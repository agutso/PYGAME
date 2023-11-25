class Cars():
    def __init__(self,year,mark,speed, tipo):
        self.year = year
        self.mark = mark
        self.speed = speed
        self.tipo = tipo
class Nisan(Cars):
    colour = "Yellow"

car1 = Nisan("2008","Nisan","200KMH","Race car")
print(car1.year,car1.colour,car1.mark,car1.speed,car1.tipo)