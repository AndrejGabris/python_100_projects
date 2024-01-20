import math

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = area / cover
    round_up_cans = math.ceil(number_of_cans) # round to next higher int number
    print(f"Number of cans needed: {round_up_cans}")

paint_calc(height=2, width=4, cover=5)




while True:
    print("Insert a number: ")
    n = int(input())

    dividable_numbers = []
    for number in range(2, n):
        if n % number == 0:
            dividable_numbers.append(number)

    if n == 1:
        print(f"Number: {n}, is not a prime number.")
    elif not dividable_numbers == []:
        print(f"Number: {n}, is not a prime number. It's dividable by {dividable_numbers}")
    elif dividable_numbers == []:
        print(f"Number: {n}, is a prime number.") 
    
