class Employee:

    def __init__(self,first_name,last_name,annual_package):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_package = annual_package
    
    def give_raise(self,increment=""):
        if increment:
            self.annual_package += increment
        else:
            self.annual_package += 5000
