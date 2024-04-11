import random


def binary_numbers_conversions():
    number = random.randint(0, 256)
    answer = input(f"represent {number} in binary (start with the first 1): ")
    result = bin(number)
    if result == "0b" + answer:
        print("Your answer is correct!")
    else:
        print(f"Wrong answer, the correct answer is {result}")


def binary_numbers_addition(): ...


def main():
    binary_numbers_conversions()


if __name__ == "__main__":
    main()
