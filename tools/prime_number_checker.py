def prime_checker(number):
    is_prime = True

    #O(n) complexity
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break
    
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


number = int(input("Give a number: "))

prime_checker(number)