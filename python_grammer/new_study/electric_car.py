# 由于ElectricCar是Car的子类，所以单独存储为1个模块时，需要用from...import...访问car.py的Car类
from python_grammer.new_study.car import Car

class ElectricCar(Car):
        
    def __init__(self,brand,model,year,battery_size):   #这里的_init_方法是初始化最大集合
        super().__init__(brand,model,year)              #super()方法调用父类的属性
        self.battery = Battery(battery_size)            #self.battery 创建电车自己的属性

    def fills_gas_tank(self):
        print(f"This car doesn't need a gas tank")

class Battery:
    def __init__(self,battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car's battery has {self.battery_size} kwh.")  
    
    def get_range(self):
        if self.battery_size == 40:
            max_miles = 150
        elif self.battery_size > 40:
            max_miles = 250
        print(f"This car's max miles is {max_miles} miles")
    
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65