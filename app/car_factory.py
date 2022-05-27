import random
import time

from app.model import Car

class CarFactory:
    def __init__(self) -> None:
        self.cars = [
            Car(brand="BMW", model="X3", doors=4),
            Car(brand="BMW", model="M5", doors=4),
            Car(brand="Audi", model="Quattro", doors=4),
            Car(brand="Renault", model="Twingo", doors=4),
            Car(brand="Audi", model="TT", doors=4),
            Car(brand="VW", model="T5", doors=3),
            Car(brand="VW", model="Golf", doors=4)
        ]

    def produce(self) -> Car:
        duration = random.randint(0, 3)
        time.sleep(duration)
        index = random.randrange(0, len(self.cars), 1)
        return self.cars[index]
