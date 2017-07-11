'''
Prime Numbers - a whole number greater than 1 that is only wholly divisible by itself or 1
Meaning no other number besides the main number or 1 should be able to be used to fully divide the main number
If num is fully divisible by any other number (meaning no remainder after the division, then num isn't prime)

The code below takes a range of numbers and generates a separate list for both prime and non-prime numbers
'''

def isprime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:  # modulus operator
                # return 'is not a prime number. Its first divisible whole number is {}'.format(x)
                # print(num, "is not a prime number")
                # print(i, "times", num // i, "is", num)
                return False
        else:
            return True
    else:
        return False
        # print('The number you entered is {}. Please enter a number that is greater than 1'.format(n))

primeNumbers = []
notPrimeNumbers = []

# print('{} {}'.format(n, (isprime(n))))
for num in range(1, 50):
    if isprime(num) is True:
        # print('{} is a prime number'.format(n))
        primeNumbers.append(num)
    elif isprime(num) is False:
        # print('{} is not a prime number'.format(n))
        notPrimeNumbers.append(num)

print('The list of prime numbers is {}'.format(primeNumbers))
print('The list of non-prime numbers is {}'.format(notPrimeNumbers))

##
