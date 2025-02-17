from axiompy import Units

units = Units()

class Converter:
    def __init__(self, n, u):
        self.n = n #Magnitude
        self.u = u #Unit
    def conv(self):
        user=int(input('''Choose the below units to convert to: 
              1. inches
              2. feet
              3. yards
              4. miles
              5. kilometers
              6. meters
              7. centimeters
              8. millimeters
                    '''))
        match user:
            case 1:
                print(units.unit_convert(self.n * units.unit(self.u), units.inch))
            case 2:
                print(units.unit_convert(self.n * units.unit(self.u), units.foot))
            case 3:
                print(units.unit_convert(self.n * units.unit(self.u), units.yard))
            case 4:
                print(units.unit_convert(self.n * units.unit(self.u), units.mile))
            case 5:
                print(units.unit_convert(self.n * units.unit(self.u), units.kilometer))
            case 6:
                print(units.unit_convert(self.n * units.unit(self.u), units.meter))
            case 7:
                print(units.unit_convert(self.n * units.unit(self.u), units.centimeter))
            case 8:
                print(units.unit_convert(self.n * units.unit(self.u), units.millimetre))
            case _:
                print("Invalid Input")


user_len=float(input('Enter magnitude: '))
user=input('''Enter the below units as per your input: 
        1. inch
        2. foot
        3. yard
        4. mile
        5. kilometer
        6. meter
        7. centimeter
        8. millimetre
           ''')

c=Converter(user_len, user)
c.conv()

    
    