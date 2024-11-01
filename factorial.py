n = int(input("Enter number:")) # Enter a valid integer number
factorial = 1 # Initialize the value of factorial as 1
while(n > 0): # check if the number is greater than zero or not 
    factorial = factorial * n # does the multiplication operation
    n = n - 1 # decrease the value of the n by 1
print(f"Factorial of the number is: {factorial}") # print the calculated value of the factorial