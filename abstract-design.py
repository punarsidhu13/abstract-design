class Toyota:
    def __init__(self, car = None):
        self.car = car
    
    def show_car(self):
        car = self.car()
        print("we have {car} and its release date is {car.release_date()}")

print("---------------------------------------------")
class Innova:
    def __init__(self, rlease_date, model, engine_cc , engine_cylinders, color):
        self.rlease_date = rlease_date
        self.model = model
        self.engine_cc= engine_cc
        self.engine_cylinders = engine_cylinders
        self.color = color

    def release_date(self):
        return self.rlease_date

    def model_car(self):
        return self.model

    def engine_capacity(self):
        return self.engine_cc

    def cylinders(self):
        return self.engine_cylinders
    
    def colors(self):
        return self.color

x = Innova( "03/09/2017", "crysta",  "2800cc",  "4", ["space gray", "silver", "White", "Black"])
a = x.release_date()
b = x.model_car()
print("Release date of innova was ",a)
print("model of the car is", b)

print("---------------------------------------------")
class LandCruiser:
    def __init__(self, rlease_date, model, engine_cc , engine_cylinders, color):
        self.rlease_date = rlease_date
        self.model = model
        self.engine_cc= engine_cc
        self.engine_cylinders = engine_cylinders
        self.color = color

    def release_date(self):
        return self.rlease_date

    def model_car(self):
        return self.model

    def engine_capacity(self):
        return self.engine_cc

    def cylinders(self):
        return self.engine_cylinders
    
    def colors(self):
        return self.color


x = LandCruiser ( "2021", "lc300",  "3600cc",  "6", ["space gray", "silver", "White", "Black"])
a = x.release_date()
b = x.model_car()
print("Release date of Land cruiser was ",a)
print("model of the car is", b)


print("---------------------------------------------")
class Hicross:
    def __init__(self, rlease_date, model, engine_cc , engine_cylinders, color):
        self.rlease_date = rlease_date
        self.model = model
        self.engine_cc= engine_cc
        self.engine_cylinders = engine_cylinders
        self.color = color

    def release_date(self):
        return self.rlease_date

    def model_car(self):
        return self.model

    def engine_capacity(self):
        return self.engine_cc

    def cylinders(self):
        return self.engine_cylinders
    
    def colors(self):
        return self.color

x = Hicross( "2023", "Innova Hicross",  "2500cc",  "4", ["space gray", "silver", "White", "Black"])
a = x.release_date()
b = x.model_car()
print("Release date of innova was ",a)
print("model of the car is", b)

print("---------------------------------------------")
class Camry:
    def __init__(self, rlease_date, model, engine_cc , engine_cylinders, color):
        self.rlease_date = rlease_date
        self.model = model
        self.engine_cc= engine_cc
        self.engine_cylinders = engine_cylinders
        self.color = color

    def release_date(self):
        return self.rlease_date

    def model_car(self):
        return self.model

    def engine_capacity(self):
        return self.engine_cc

    def cylinders(self):
        return self.engine_cylinders
    
    def colors(self):
        return self.color



x = Camry( "2019", "Camry Hybrid",  "3000cc",  "6", ["space gray", "silver", "White", "Black"])
a = x.release_date()
b = x.model_car()
print("Release date of Camry was ",a)
print("model of the car is", b)

print("---------------------------------------------")
 