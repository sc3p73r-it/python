class Vehicle:
    def vehicle(self):
        print("A vechile is a machine that trasnports people or cargo..")

class Car(Vehicle):
    def car(self):
        print(" A car is it give for the freedom to travel.")

class Train(Vehicle):
    def train(self):
        print("Traveling by train can be convenient")

obj_car = Car()
obj_train = Train()

obj_car.vehicle()
obj_car.car()

obj_train.vehicle()
obj_train.train()