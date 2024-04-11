import random


def binary_numbers_conversions():
    number = random.randint(0, 256)
    answer = input(f"represent {number} in binary (start with the first 1): ")
    result = bin(number)
    if result == "0b" + answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is {result.replace("b", "0")}.")


def binary_numbers_addition(): 
    first_number = random.randint(0,256)
    second_number = random.randint(0,256)
    answer = input(f"{bin(first_number).replace("b", "0")} \
+ {bin(second_number).replace("b", "0")} = ")
    result = bin(first_number + second_number).replace("b", "0")
    if result == answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is {result}.")


def main():
    binary_numbers_conversions()
    binary_numbers_addition()


if __name__ == "__main__":
    main()
