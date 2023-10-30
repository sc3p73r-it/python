class Desktop:
    def desk(self):
        print("Desktop can add more storage, RAM and a better graphics.")

class Laptop:
    def lap(self):
        print("Lap are best used for light work: reading, word processing.")

class Dell(Desktop,Laptop):
    def dell(self):
        print("Dell is one of the world's largest PC manufactures.")
    
obj = Dell()
obj.desk()
obj.lap()
obj.dell()
