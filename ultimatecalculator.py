import math
from image import art
import os

run = True

while run:
  def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

  def calculate_area_rectangle(length, breadth):
    area = length * breadth
    return area

  def calculate_area_triangle(base, height):
    area = 0.5 * base * height
    return area

  def calculate_area_square(side):
    area = side * side
    return area

  def calculate_area_parallelogram(base, height):
    area = base * height
    return area

  def main():
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
    print("8. Quadratic equations")
    print("Quit - Ctrl + C")
    print("   ")
    choice = int(input("Please select an equation to solve: "))

    if choice == 1:
      calculate_addition()
    elif choice == 2:
      calculate_subtraction()
    elif choice == 3:
      calculate_multiplication()
    elif choice == 4:
      calculate_division()
    elif choice == 5:
      calculate_exponentiation()
    elif choice == 6:
      calculate_logarithm()
    elif choice == 7:
      calculate_trigonometry()
    elif choice == 8:
      # Areas of different shapes
      print("1. Circle")
      print("2. Rectangle")
      print("3. Triangle")
      print("4. Square")
      print("5. Parallelogram")
      print("Quit - Ctrl + C")
      
      print("   ")
      print("   ")
      
      shape = int(input("Enter the number of the shape whose area you want to find: "))
      if shape == 1:
        radius = float(input("Enter the radius of the circle: "))
        print("   ")
        print("The area of the circle is", calculate_area_circle(radius))
        
        
      elif shape == 2:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        print("   ")
        print("The area of the rectangle is", calculate_area_rectangle(length, breadth))
        
        
      elif shape == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("   ")
        print("The area of the triangle is", calculate_area_triangle(base, height))
        
        
      elif shape == 4:
        side = float(input("Enter the side of the square: "))
        print("   ")
        print("The area of the square is", calculate_area_square(side))
        
        
      elif shape == 5:
        base = float(input("Enter the base of the parallelogram: "))
        height = float(input("Enter the height of the parallelogram: "))
        print("   ")
        print("The area of the parallelogram is", calculate_area_parallelogram(base, height))
        
        
      else:
        print("   ")
        print("   ")
        print("Sorry, I don't know the area of that shape.")
        
        
    else:
      print("Invalid choice.")

  def calculate_addition():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(x, "+", y, "=", x + y)


  def calculate_subtraction():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(x, "-", y, "=", x - y)


  def calculate_multiplication():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(x, "*", y, "=", x * y)


  def calculate_division():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(x, "/", y, "=", x / y)


  def calculate_trigonometry():
    _type_ = input('What trigonometry function do you want to use (sin, cos, cosine, tan, cot, sec): ')
    value = input('Value: ')
    value = int(value)
    if _type_ == "sin":
      print(math.sin(value))
    elif _type_ == "tan":
      print(math.tan(value))
    elif _type_ == "cos":
      print(math.cos(value))
    elif _type_ == "sec":
      print(math.acos(value))
    elif _type_ == "cosec":
      print(math.asin(value))
    elif _type_ == "cot":
      print(math.atan(value))
    else:
      print("The type isn't correct.")


  main()
  ask = input('Do you want to continue(Y/N): ')
  if ask.lower() == 'y':
    run = True
  else:
    run = False
