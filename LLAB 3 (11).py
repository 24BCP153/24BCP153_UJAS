degree = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
radian_x = degree * (3.14159 / 180)
print(f"{degree} degrees is equal to {radian_x} radians.")

sinx = radian_x - pow(radian_x ,3)/ 6  
print(sinx)

                                                 
