class Vehicle:
    #Constructor
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240,18)
print(f"ModelX has maximum speed {modelX.max_speed} km/h and it has mileage of { modelX.mileage}")