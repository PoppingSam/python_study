class Car:


    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.miles = 0


    def get_description(self):
        long_name = f"{self.year} {self.brand} {self.model}"
        return long_name.title()
    

    def read_miles(self):
        print(f"This car drives {self.miles} miles")

    
    def update_miles(self,miles):
        if miles >= self.miles:
            self.miles = miles
        else:
            print("You cannot return back")
    

    def increment_miles(self,increment):
        self.miles += increment

    def fills_gas_tank(self):
        print(f"This car need a gas tank")
