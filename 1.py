def func(x,y) :
    return x**2 + 2*x*y + y**2 

print(func(10,5))
#######################################
PI = 3.14159

def circle(r):
    return PI*r**2

r = float(input("Enter the value of radius : "))

print( "{:.2f}".format(circle(r)))

##########################################

def farenheit(C):
    return (C * 9/5) + 32

celcius = float(input("Enter the value of Celsius : "))
print(f"Farenheit:{farenheit(celcius):.2f}")
##########################################