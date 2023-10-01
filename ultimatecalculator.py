import math
from image import art


def calculate_addition(num_1, num_2):
    value = num_1 + num_2
    print(f"{num_1} + {num_2} = {value}")


def calculate_subtraction(num_1, num_2):
    value = num_1 - num_2
    print(f"{num_1} - {num_2} = {value}")


def calculate_multiplication(num_1, num_2):
    value = num_1 * num_2
    print(f"{num_1} * {num_2} = {value}")


def calculate_division(num_1, num_2):
    value = num_1 / num_2
    print(f"{num_1} / {num_2} = {value}")


def calculate_logarithm(base, num):
    value = math.log(num, base)
    print(f"log of {num} with base {base} = {value}")


def calculate_exponentiation(base, exponent):
    value = math.pow(base, exponent)
    print(f"{base} to the power {exponent} = {value}")


def calculate_trigonometry(_type_, num):    
    if _type_ == 1:
        value = math.sin(num)
        print(f"{_type_} {num} = {value}")
    elif _type_ == 2:
        value = math.tan(num)
        print(f"{_type_} {num} = {value}")
    elif _type_ == 3:
        value = math.cos(num)
        print(f"{_type_} {num} = {value}")
    elif _type_ == 4:
        value = math.acos(num)
        print(f"{_type_} {num} = {value}")
    elif _type_ == 5:
        value = math.asin(num)
        print(f"{_type_} {num} = {value}")
    elif _type_ == 6:
        value = math.atan(num)
        print(f"{_type_} {num} = {value}")
    else:
        print("The type isn't correct.")


def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    print(f"Area of circle of radius {radius} is {area} unit square") 


def calculate_area_rectangle(length, breadth):
    area = length * breadth
    print(f"Area of rectangle of length {length} and breadth {breadth} is {area} unit square") 


def calculate_area_triangle(base, height):
    area = 0.5 * base * height
    print(f"Area of triangle of base {base} and height {height} is {area} unit square") 


def calculate_area_square(side):
    area = side * side
    print(f"Area of square of side {side} is {area} unit square") 


def calculate_area_parallelogram(base, height):
    area = base * height
    print(f"Area of parallelogram of base {base} and height {height} is {area} unit square") 



def main():
    while True:
        try:
            print(art)
            print("Welcome to the mathematical equation solver!")
            print("Here are the equations that I can solve:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Trigonometry")
            print("8. Area of Shapes")
            print("Quit - Ctrl + C")
            print()
            choice = int(input("Please select an equation to solve: "))
            if _type_ in [1,2,3,4,5,6,7,8]:
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

    if choice < 5:
        while True:
            try:
                num_1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input")
        while True:
            try:
                num_2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input")

        if choice == 1:
            calculate_addition(num_1)
            
        elif choice == 2:
            calculate_subtraction(num_1)
            
        elif choice == 3:
            calculate_multiplication(num_1)
            
        elif choice == 4:
            calculate_division(num_1)
        
    elif choice == 5:
        while True:
            try:
                base = float(input("Enter the base number: "))
                break
            except ValueError:
                print("Invalid input")
        while True:
            try:
                num = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid input")
        calculate_exponentiation(base, num)
        
    elif choice == 6:
        while True:
            try:
                base = float(input("Enter the base number: "))
                break
            except ValueError:
                print("Invalid input")
        while True:
            try:
                exponent = float(input("Enter the exponent number: "))
                break
            except ValueError:
                print("Invalid input")
        calculate_logarithm(base, exponent)
        
    elif choice == 7:
        while True:
            try:
                print("What trigonometry function do you want to use:")
                print("1. sin")
                print("2. cos")
                print("3. cosine")
                print("4. tan")
                print("5. cot")
                print("6. sec")
                print()
                _type_ = int(input("Please select a function to solve: ")).lower()
                if _type_ in [1,2,3,4,5,6]:
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")
        while True:
            try:
                exponent = float(input("Enter the Number: "))
                break
            except ValueError:
                print("Invalid input")
        calculate_trigonometry(_type_, num)
        
    elif choice == 8:
        # Areas of different shapes
        while True:
            try:
                print("What is the shape:")
                print("1. Circle")
                print("2. Rectangle")
                print("3. Triangle")
                print("4. Square")
                print("5. Parallelogram")
                print()
                shape = int(input("Please enter the number of shape whose area you want to find: "))
                if _type_ in [1,2,3,4,5]:
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")

        if shape == 1:
            radius = float(input("Enter the radius of the circle: "))
            print()
            calculate_area_circle(radius)

        elif shape == 2:
            length = float(input("Enter the length of the rectangle: "))
            breadth = float(input("Enter the breadth of the rectangle: "))
            print()
            calculate_area_rectangle(length, breadth)

        elif shape == 3:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print()
            calculate_area_triangle(base, height)

        elif shape == 4:
            side = float(input("Enter the side of the square: "))
            print()
            calculate_area_square(side)

        elif shape == 5:
            base = float(input("Enter the base of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            print()
            calculate_area_parallelogram(base, height)  

run = True
while run:
    main()
    while True:
        ask = input('Do you want to continue(Y/N): ')
        if ask.lower() == 'n':
            print("Bye! Have a great time!")
            run = False
            break
        elif ask.lower() == 'y':
            break
        else:
            print("Invalid input")

