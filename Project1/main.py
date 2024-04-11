import random


def binary_numbers_conversions():
    number = random.randint(0, 256)
    answer = input(f"represent {number} in binary (start with the first 1): ")
    result = bin(number)
    if result[2:] == answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is \
{result[2:]}.")


def binary_numbers_addition(): 
    first_number = random.randint(0, 256)
    second_number = random.randint(0, 256)
    answer = input(f"{bin(first_number)[2:]} \
+ {bin(second_number)[2:]} = ")
    result = bin(first_number + second_number)
    if result[2:] == answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is {result[2:]}.")


def hex_numbers_conversions():
    number = random.randint(0, 256)
    answer = input(f"represent {number} in hexadecimal (use small letters): ")
    result = hex(number)
    if result[2:] == answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is \
{result[2:]}.")


def octal_numbers_conversions():
    number = random.randint(0, 256)
    answer = input(f"represent {number} in octal: ")
    result = oct(number)
    if result[2:] == answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is \
{result[2:]}.")


def main():
    binary_numbers_conversions()
    binary_numbers_addition()
    hex_numbers_conversions()
    octal_numbers_conversions()


if __name__ == "__main__":
    main()
