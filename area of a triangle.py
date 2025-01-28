# Function to calculate the area of a triangle using base and height
def area_with_base_height(base, height):
    return 0.5 * base * height

# Function to calculate the area of a triangle using Heron's formula
def area_with_sides(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Example usage
if __name__ == "__main__":
    print("Choose the method to calculate the area of a triangle:")
    print("1. Using base and height")
    print("2. Using the lengths of three sides")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_with_base_height(base, height)}")
    elif choice == 2:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        print(f"The area of the triangle is: {area_with_sides(a, b, c)}")
    else:
        print("Invalid choice. Please run the program again.")