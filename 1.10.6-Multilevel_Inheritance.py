class Vehicle:
    def vehicle(self):
        print("A vehicle is a machine that transports people to go.")

class Car(Vehicle):
    def car(self):
        print("A car is it gives that freedom to travel.")

class BMW(Car):
    def bmw(self):
        print("BMW is performance and luxury models.")

obj = BMW()
obj.vehicle()
obj.car()
obj.bmw()