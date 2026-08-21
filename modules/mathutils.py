def perimeter_rectangle():
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    return 2*(l + b)

def area_circle():
    r = int(input("Enter radius: "))
    return 3.14*(r**2)

if __name__ == "__main__":
    print(f"Testing: {perimeter_rectangle()}")
    print(f"Testing: {area_circle()}")
