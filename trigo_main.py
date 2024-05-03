import math as m
import numpy as np

def Sn(x):
    sn = m.sin(x)
    return sn

def Cs(x):
    Cs = m.cos(x)
    return Cs

def Tn(x):
    tan_x = m.tan(x)
    if m.cos(x) == 0:
        print("Tangent is undefined for this angle.")
        return None
    else:
        Tn = tan_x
        return Tn

def Sec(x):
    cos_x = m.cos(x)
    if cos_x == 0:
        print("Secant is undefined for this angle.")
        return None
    else:
        Sec = 1 / cos_x
        return Sec

def Csc(x):
    sin_x = m.sin(x)
    if sin_x == 0:
        print("Cosecant is undefined for this angle.")
        return None
    else:
        Csc = 1 / sin_x
        return Csc

def Cot(x):
    tan_x = m.tan(x)
    if m.sin(x) == 0:
        print("Cotangent is undefined for this angle.")
        return None
    else:
        Cot = 1 / tan_x
        return Cot

def menu():
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    print("4. Secant")
    print("5. Cosecant")
    print("6. Cotangent")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    for i in range(999999):
        choice = menu()
        if choice == 1:
            print("\n\nNote: If you want to enter the value in radian then write it using numpy module e.g. np.pi/2 or 3*np.pi/2.\nIf you want to enter the value in degree then write it as it is e.g. 90 or 270.\n")
            print("enter the unit")
            print("1. Radian")
            print("2. Degree")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                x = input("Enter the value of x: ")
                #x = eval(x)
                sn = Sn(x)
                print(f"Sine of {x:.3f} is {sn:.2f}")
            elif ch == 2:
                x = input("Enter the value of x: ")
                x = eval(x)
                #x = m.degrees(x)
                sn = Sn(m.radians(float(x)))
                print(f"Sine of {int(x)} is {sn:.2f}°")
            else:
                print("Invalid choice")
        elif choice == 2:
            print("Note: If you want to enter the value in radian then write it using numpy module e.g. np.pi/2 or 3*np.pi/2.\nIf you want to enter the value in degree then write it as it is e.g. 90 or 270.")
            print("enter the unit")
            print("1. Radian")
            print("2. Degree")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                x = input("Enter the value of x: ")
                x = eval(x)
                cs = Cs(x)
                print(f"Cosine of {x:.3f} is {cs:.2f}")
            elif ch == 2:
                x = input("Enter the value of x: ")
                x = eval(x)
                #x = int(m.degrees(x))
                cs = Cs(m.radians(float(x)))
                print(f"Cosine of {(x)} is {cs:.2f}°")
            else:
                print("Invalid choice")
        elif choice == 3:
            print("Note: If you want to enter the value in radian then write it using numpy module e.g. np.pi/2 or 3*np.pi/2.\nIf you want to enter the value in degree then write it as it is e.g. 90 or 270.")
            print("enter the unit")
            print("1. Radian")
            print("2. Degree")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                x = input("Enter the value of x: ")
                x = eval(x)
                tn = Tn(x)
                if tn is not None:
                    print(f"Tangent of {x:.3f} is {tn:.2f}")
            elif ch == 2:
                x = input("Enter the value of x: ")
                x = eval(x)
                #x = int(m.degrees(x))
                tn = Tn(m.radians(float(x)))
                if tn is not None:
                    print(f"Tangent of {(x)} is {tn:.2f}°")
            else:
                print("Invalid choice")
        elif choice == 4:
            print("Note: If you want to enter the value in radian then write it using numpy module e.g. np.pi/2 or 3*np.pi/2.\nIf you want to enter the value in degree then write it as it is e.g. 90 or 270.")
            print("enter the unit")
            print("1. Radian")
            print("2. Degree")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                x = input("Enter the value of x: ")
                x = eval(x)
                sec = Sec(x)
                if sec is not None:
                    print(f"Sec of {x:.3f} is {sec:.2f}")
            elif ch == 2:
                x = input("Enter the value of x: ")
                x = eval(x)
                #x = int(m.degrees(x))
                sec = Sec(m.radians(float(x)))
                if sec is not None:
                    print(f"Sec of {(x)} is {sec:.2f}°")
            else:
                print("Invalid choice")
        elif choice == 5:
            print("Note: If you want to enter the value in radian then write it using numpy module e.g. np.pi/2 or 3*np.pi/2.\nIf you want to enter the value in degree then write it as it is e.g. 90 or 270.")
            print("enter the unit")
            print("1. Radian")
            print("2. Degree")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                x = input("Enter the value of x: ")
                x = eval(x)
                csc = Csc(x)
                if csc is not None:
                    print(f"Cosec of {x:.3f} is {csc:.2f}")
            elif ch == 2:
                x = input("Enter the value of x: ")
                x = eval(x)
                #x = int(m.degrees(x))
                csc = Csc(m.radians(float(x)))
                if csc is not None:
                    print(f"Cosec of {(x)} is {csc:.2f}°")
            else:
                print("Invalid choice")
        elif choice == 6:
            print("Note: If you want to enter the value in radian then write it using numpy module e.g. np.pi/2 or 3*np.pi/2.\nIf you want to enter the value in degree then write it as it is e.g. 90 or 270.")
            print("enter the unit")
            print("1. Radian")
            print("2. Degree")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                x = input("Enter the value of x: ")
                x = eval(x)
                cot = Cot(x)
                if cot is not None:
                    print(f"Cot of {x:.3f} is {cot:.2f}")
            elif ch == 2:
                x = input("Enter the value of x: ")
                x = eval(x)
                
                cot = Cot(m.radians(float(x)))
                if cot is not None:
                    print(f"Cot of {(x)} is {cot:.2f}°")
            else:
                print("Invalid choice")
        elif choice == 7:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
