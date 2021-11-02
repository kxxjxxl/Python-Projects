class Car:

    def __init__(self, make, model, color, year):
        self._make = make
        self._model = model
        self._color = color
        self._year = year


    def drive(self):
        print("This " + self._model +" is driving")


