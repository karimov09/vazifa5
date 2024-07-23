from nmk import NMK, abstractmethod

class Engine(NMK):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Ve(Engine):
    def turn_on(self):
        print()
    def turn_off(self):
        print()
class Car(Engine):
    def turn_on(self):
        print()
    def turn_off(self):
        print()
ve = Ve()
ve.turn_on()   
ve.turn_off()  
car = Car()
car.turn_on()    
car.turn_off()   
