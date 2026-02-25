import shape
print("Choose Shape")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = float(input("Enter your choice (1-3):"))

if choice == 1 :
    r = float(input("Enter the radius:"))
    area = shape.area_circle(r)
    print("The area of Circle is:" , area) 
    

elif choice ==2 :
    l = float(input("Enter the length:"))
    w = float(input("Enter the width:"))
    area = shape.area_rectangle(l,w)
    print("The area of the reactangle is:" , area)

elif choice == 3 :
    b = float(input("Enter the base:"))
    h = float(input("Enter the height:"))
    area = shape.area_triangle(b,h)  
    print("The area of the triangle is:" , area)  

else :
    print("Invalid choice")
    
