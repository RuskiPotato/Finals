class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"Driving {self.brand} {self.model}"

class SchoolBus(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def drive(self):
        return f"Driving school bus with {self.capacity} students"