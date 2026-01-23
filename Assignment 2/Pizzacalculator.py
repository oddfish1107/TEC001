Pizza1_Diameter, Pizza1_Price = map(int, input("Enter Pizza 1's Diameter and Price: ").split())
Pizza2_Diameter, Pizza2_Price = map(int, input("Enter Pizza 2's Diameter and Price: ").split())

def True_Value_Finder(Diameter, Price):
    Meter = Diameter / 100
    Area = ((Meter/2)**2)*3.14
    Value = Price/Area
    return Value

Value1 = True_Value_Finder(Pizza1_Diameter, Pizza1_Price)
Value2 = True_Value_Finder(Pizza2_Diameter, Pizza2_Price)

if Value1 > Value2:
    print("Pizza 2 is a better deal")
else:
    print("Pizza 1 is a better deal")



