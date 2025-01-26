# Simple program to multiply two numbers
def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The product is: {multiply_numbers(num1, num2)}")
