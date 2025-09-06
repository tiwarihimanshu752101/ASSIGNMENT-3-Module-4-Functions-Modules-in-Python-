def factorial(n):     # using loop recursion function
    if n==0 or n==1:
        return 1
    else:
        result = n*factorial(n-1)
        return result
    
num = int(input("Enter the number: "))

print("Factorial of",num,"is:",factorial(num))