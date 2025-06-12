class Car:
    count = 0

    def __init__(self, name="", speed=0):
        self.name = name
        self.speed = speed
        Car.count = Car.count + 1

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def upSpeed(self, value):
        self.speed = self.speed + value

    def downSpeed(self, value):
        self.speed = self.speed - value


car1 = Car("소나타", 30)
car2 = Car("아반떼", 20)

car1.upSpeed(10)
car2.downSpeed(5)

print("자동차 1 - 이름: " + car1.getName() + ", 속도: " + str(car1.getSpeed()))
print("자동차 2 - 이름: " + car2.getName() + ", 속도: " + str(car2.getSpeed()))
print("총 생산된 자동차 수: " + str(Car.count))
