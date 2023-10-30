class Vehicle:
    def vehicle(self):
      print("A vechile is a machine that trasnports people or cargo..")

class Car(Vehicle):
    def car(self):
     print(" A car is it give for the freedom to travel.")

class Train(Vehicle):
    def train(self):
         print("Traveling by train can be convenient")

class BMW(Car,Vehicle):
    def bmw(self):
        print("BMW is performance and luxury models.")

obj_train = Train()
obj_bmw = BMW()

obj_train.vehicle()
obj_train.train()

obj_bmw.vehicle()
obj_bmw.car()
obj_bmw.bmw()


