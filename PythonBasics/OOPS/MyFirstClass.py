class Bike:
    # Attributes of Class
    color = None
    tyre_size = None
    price = None
    fuel_type = None

    # Behaviour of the Class
    def ride_type(self):
        print("Move Forward")

    def explain_attr(self):
        print(f"Color is - ", self.color)
        print(f"Tyre Size is - ", self.tyre_size)
        print(f"Price is - ", self.price)
        print(f"Fuel Type is - ", self.fuel_type)

bike1 = Bike()
bike1.color = "Blue"
bike1.explain_attr()

bike2 = Bike()
bike2.color = "Silver"
bike2.explain_attr()
