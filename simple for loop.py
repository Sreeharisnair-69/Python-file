number = int(input("Enter a number:"))
isPrime = True
for i in range(2,(number//2) + 1):
    if(number % i == 0):
        isPrime = False
        break
if isPrime == True:
    print(f"The given number {number} is prime")
else:
    print(f"The given number {number} is not prime")