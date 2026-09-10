# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number: "))

# sum = num1 + num2 
# print("The sum of two numbers is: ", sum)
# print("The sum of two numbers is "+ str(sum))

# diff = num1 - num2 
# print("The difference of two numbes is: ",diff)

# mul =  num1*num2
# print("The product of two numbers is: ",mul)

# div = num1/num2
# print("The division of two numbers is: ",div)

# n = int(input("Enter a number: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a+b
#     a = b
#     b = c

# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1,n+1):
#     factorial = factorial *i
#     i= i+1

# print("The factorial of number is ",factorial)

def arithmetic_operation():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nResult:")
        print("Sum: ",num1+num2)
        print("Difference: ",num1-num2)
        print("Multiply: ",num1*num2)
        if(num2!=0):
            print("Division: ",num1/num2)
        else:
            print("Divison by zero is not possible")

    except ValueError:
        print("Please enter valid numbers")

arithmetic_operation()


