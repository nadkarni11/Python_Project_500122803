import math as m
import trigo_main as tg


def circle_area(radius):
    return m.pi * radius ** 2

def circle_circumference(radius):
    return 2 * m.pi * radius

def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def cube_volume(side):
    return side ** 3

def cube_surface_area(side):
    return 6 * side ** 2

def sphere_volume(radius):
    return 4/3 * m.pi * radius ** 3

def sphere_surface_area(radius):
    return 4 * m.pi * radius ** 2

def cylinder_volume(radius, height):
    return m.pi * radius ** 2 * height

def cylinder_surface_area(radius, height):
    return 2 * m.pi * radius * (radius + height)

def cylinder_curved_surface_area(radius, height):
    return 2 * m.pi * radius * height

def cone_volume(radius, height):
    return 1/3 * m.pi * radius ** 2 * height

def cone_surface_area(radius, height):
    return m.pi * radius * (radius + m.sqrt(radius ** 2 + height ** 2))

def cone_curved_surface_area(radius, height):
    return m.pi * radius * m.sqrt(radius ** 2 + height ** 2)

def prsim_volume(base_area, height):
    return base_area * height

def prism_surface_area(base_perimeter, base_area, height):
    return base_perimeter * height + 2 * base_area

def pyramid_volume(base_area, height):
    return 1/3 * base_area * height

def pyramid_surface_area(base_perimeter, slant_height):
    return 0.5 * base_perimeter * slant_height

def hemisphere_volume(radius):
    return 2/3 * m.pi * radius ** 3

def hemisphere_surface_area(radius):
    return 3 * m.pi * radius ** 2

def menu():
    print("Welcome to the Geometry Calculator!")
    print("Choose the calculate: ")
    print("1.Geometry")
    print("2.Trigonometry")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        print("Welcome to the Geometry Calculator!")
        print ("Choose the shape you want to calculate")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Triangle")
        print("5. Cube")
        print("6. Sphere")
        print("7. Cylinder")
        print("8. Cone")
        print("9. Prism")
        print("10. Pyramid")
        print("11. Hemisphere")
        print("12. Exit")
        choice = int(input("Enter your choice: "))
        return choice
    elif choice==2:
        tg.main()
    elif choice==3:
        print("Exited successfully!")
        exit()

def main():
    for i in range(9999999):
        choice = menu()
        if choice == 1:
            print("1. area")
            print("2. circumference")
            ch=int(input("Enter your choice: "))
            if ch==1:
                radius = float(input("Enter the radius of the circle: "))
                print("Area of the circle is: ", circle_area(radius))
            elif ch==2:
                radius = float(input("Enter the radius of the circle: "))
                print("Circumference of the circle is: ", circle_circumference(radius))
        elif choice == 2:
            print("1. area")
            print("2. perimeter")
            ch=int(input("Enter your choice: "))
            if ch==1:
                side = float(input("Enter the side of the square: "))
                print("Area of the square is: ", square_area(side))
            elif ch==2:
                side = float(input("Enter the side of the square: "))
                print("Perimeter of the square is: ", square_perimeter(side))
        elif choice == 3:
            print("1. area")
            print("2. perimeter")
            ch=int(input("Enter your choice: "))
            if ch==1:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                print("Area of the rectangle is: ", rectangle_area(length, width))
            elif ch==2:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                print("Perimeter of the rectangle is: ", rectangle_perimeter(length, width))
        elif choice == 4:
            print("1. area")
            print("2. perimeter")
            ch=int(input("Enter your choice: "))
            if ch==1:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                print("Area of the triangle is: ", triangle_area(base, height))
            elif ch==2:
                side1 = float(input("Enter the side1 of the triangle: "))
                side2 = float(input("Enter the side2 of the triangle: "))
                side3 = float(input("Enter the side3 of the triangle: "))
                print("Perimeter of the triangle is: ", triangle_perimeter(side1, side2, side3))
        elif choice == 5:
            print("1. volume")
            print("2. surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                side = float(input("Enter the side of the cube: "))
                print("Volume of the cube is: ", cube_volume(side))
            elif ch==2:
                side = float(input("Enter the side of the cube: "))
                print("Surface area of the cube is: ", cube_surface_area(side))
        elif choice == 6:
            print("1. volume")
            print("2. surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                radius = float(input("Enter the radius of the sphere: "))
                print("Volume of the sphere is: ", sphere_volume(radius))
            elif ch==2:
                radius = float(input("Enter the radius of the sphere: "))
                print("Surface area of the sphere is: ", sphere_surface_area(radius))
        elif choice == 7:
            print("1. volume")
            print("2. surface area")
            print("3. curved surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                print("Volume of the cylinder is: ", cylinder_volume(radius, height))
            elif ch==2:
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                print("Surface area of the cylinder is: ", cylinder_surface_area(radius, height))
            elif ch==3:
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                print("Curved surface area of the cylinder is: ", cylinder_curved_surface_area(radius, height))
        elif choice == 8:
            print("1. volume")
            print("2. surface area")
            print("3. curved surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                print("Volume of the cone is: ", cone_volume(radius, height))
            elif ch==2:
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                print("Surface area of the cone is: ", cone_surface_area(radius, height))
            elif ch==3:
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                print("Curved surface area of the cone is: ", cone_curved_surface_area(radius, height))
        elif choice == 9:
            print("1. volume")
            print("2. surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                base = float(input("Enter the base of the prism: "))
                height = float(input("Enter the height of the prism: "))
                print("Volume of the prism is: ", prsim_volume(base, height))
            elif ch==2:
                base = float(input("Enter the base of the prism: "))
                height = float(input("Enter the height of the prism: "))
                print("Surface area of the prism is: ", prism_surface_area(base, base, height))
        elif choice == 10:
            print("1. volume")
            print("2. surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                base = float(input("Enter the base of the pyramid: "))
                height = float(input("Enter the height of the pyramid: "))
                print("Volume of the pyramid is: ", pyramid_volume(base, height))
            elif ch==2:
                base = float(input("Enter the base of the pyramid: "))
                slant_height = float(input("Enter the slant height of the pyramid: "))
                print("Surface area of the pyramid is: ", pyramid_surface_area(base, slant_height))
        elif choice == 11:
            print("1. volume")
            print("2. surface area")
            ch=int(input("Enter your choice: "))
            if ch==1:
                radius = float(input("Enter the radius of the hemisphere: "))
                print("Volume of the hemisphere is: ", hemisphere_volume(radius))
            elif ch==2:
                radius = float(input("Enter the radius of the hemisphere: "))
                print("Surface area of the hemisphere is: ", hemisphere_surface_area(radius))
        elif choice == 12:
            print("are you sure you want to exit? y/n")
            c=input()
            if c=="y" or c=="Y":
                print("Exited successfully!")
                break
            else:
                continue
            print("Exit")
            
        else:
            print("Invalid choice! Please try again.")
        
        print("Do you want to continue? (yes/no): ")
        c = input()
        if c.lower() == "no" or c.lower() == "n" or c.lower() == "NO" or c.lower() == "N":
            print("Thank you for using my program!")
            break
        elif c.lower() == "yes" or c.lower() == "y" or c.lower() == "YES" or c.lower() == "Y":
            continue
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()