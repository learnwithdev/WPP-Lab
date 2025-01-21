def convert_length(feet, conversion_option):
    conversions = [("inches", 12), 
                   ("yards", 1/3), 
                   ("miles", 1/5280), 
                   ("millimeters", 304.8), 
                   ("centimeters", 30.48), 
                   ("meters", 0.3048), 
                   ("kilometers", 0.0003048)]
    
    return feet * conversions[conversion_option - 1][1], conversions[conversion_option - 1][0]

# def main():
feet = float(input("Enter the length in feet: "))
print("Choose the conversion option:")
print("1. Inches")
print("2. Yards")
print("3. Miles")
print("4. Millimeters")
print("5. Centimeters")
print("6. Meters")
print("7. Kilometers")
    
option = int(input("Enter the number corresponding to your choice: "))
    
if 1 <= option <= 7:
    converted_value, unit = convert_length(feet, option)
    print(f"{feet} feet is equal to {converted_value} {unit}.")
else:
    print("Invalid option. Please choose a number between 1 and 7.")
