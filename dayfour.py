class Car:

    # remember that this automatically gets call when class is created
    # assigns
    def __init__(self, wheels, engine):
        self.wheels = wheels
        self.engine = engine

    def parts(self):
        print(f"Camry: {self.wheels} wheels & {self.engine} engine")
        return 0


# Calls the class method
camry = Car(4, 1)
print(camry.parts())

# Calls the class attribute
camry.wheels = 2
print(camry.wheels)

str = 'Learn Python!'
print(str[3:8])
